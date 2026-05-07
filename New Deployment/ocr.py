import numpy as np
import cv2
from PIL import Image, ImageDraw
import easyocr
from ultralytics import YOLO
import os

from config import MODEL_PATH, FIELD_NAMES

# load model + OCR reader once
model = YOLO(MODEL_PATH)
reader = easyocr.Reader(['en'])


def extract_fields(image_path, annotated_path=None):

    results = model(image_path)

    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    extracted_data = {}

    for r in results:

        boxes = r.boxes.xyxy.cpu().numpy()
        classes = r.boxes.cls.cpu().numpy()

        for box, cls in zip(boxes, classes):

            x1, y1, x2, y2 = map(int, box)

            field_name = FIELD_NAMES[int(cls)]

            draw.rectangle([x1, y1, x2, y2], outline=(0, 200, 0), width=3)

            # small padding
            pad = 4
            crop = img.crop((x1 + pad, y1 + pad, x2 - pad, y2 - pad))
            crop_np = np.array(crop)

            # 🔹 Upscale image for better OCR
            crop_np = cv2.resize(crop_np, None, fx=2, fy=2,
                                 interpolation=cv2.INTER_CUBIC)

            # 🔹 OCR with field-specific rules
            if field_name == "Credits":
                ocr_result = reader.readtext(
                    crop_np, allowlist="0123456789", paragraph=False)

            elif field_name == "Percentage":
                ocr_result = reader.readtext(
                    crop_np, allowlist="0123456789.", paragraph=False)

            elif field_name == "Serial No":
                ocr_result = reader.readtext(
                    crop_np,
                    allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                    paragraph=False
                )

            elif field_name == "Course Code":
                ocr_result = reader.readtext(
                    crop_np,
                    allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                    paragraph=False
                )

            else:
                ocr_result = reader.readtext(crop_np, paragraph=False)

            text = ""
            if ocr_result:
                text = ocr_result[0][1]

            # 🔹 Clean OCR text
            text = text.strip()
            text = text.replace(":", "").replace("|", "").replace("  ", " ")

            extracted_data[field_name] = text

            label = f"{field_name}: {text}"

            bbox = draw.textbbox((0, 0), label)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            draw.rectangle(
                [x1, y1 - text_height - 6, x1 + text_width + 6, y1],
                fill=(0, 200, 0)
            )

            draw.text((x1 + 3, y1 - text_height - 3), label, fill="white")

    if annotated_path:
        os.makedirs(os.path.dirname(annotated_path), exist_ok=True)
        img.save(annotated_path)

    return extracted_data
