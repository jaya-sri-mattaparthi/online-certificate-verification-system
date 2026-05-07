import Levenshtein
import re


def normalize(text):
    text = str(text).lower()

    # remove spaces and common OCR noise
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.replace(":", "")
    text = text.replace("|", "i")

    # remove unwanted characters
    text = re.sub(r"[^a-z0-9.]", "", text)

    return text.strip()


def overall_verification_accuracy(extracted_data, db_data):

    db_index = {
        "Serial No": 0,
        "Student Name": 1,
        "Course Name": 2,
        "Issued On": 3,
        "Course Code": 4,
        "Percentage": 5,
        "Credits": 6
    }

    total_mismatches = 0
    total_length = 0

    for field, idx in db_index.items():

        if not db_data:
            continue

        ocr_value = normalize(extracted_data.get(field, ""))
        db_value = normalize(db_data[idx])

        distance = Levenshtein.distance(ocr_value, db_value)
        length = max(len(ocr_value), len(db_value))

        total_mismatches += distance
        total_length += length

    if total_length == 0:
        return 100

    accuracy = (1 - total_mismatches / total_length) * 100

    return round(accuracy, 2)
