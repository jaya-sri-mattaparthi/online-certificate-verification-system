import base64
import json
import re

from huggingface_hub import InferenceClient


# ==============================
# HuggingFace API Configuration
# ==============================

HF_API_KEY = "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"

client = InferenceClient(
    api_key=HF_API_KEY
)


# ==============================
# Prompt for Vision Model
# ==============================

PROMPT = """
You are an AI system that extracts information from certificates.

Extract the following fields from the certificate image and return ONLY JSON:

{
 "Serial No": "",
 "Student Name": "",
 "Course Name": "",
 "Course Code": "",
 "Issued On": "",
 "Percentage": "",
 "Credits": ""
}

Rules:
- If a field is missing return null
- Return only JSON
"""


# ==============================
# Encode image
# ==============================

def encode_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")


# ==============================
# Extract JSON safely
# ==============================

def extract_json(text):
    try:
        match = re.search(r"\{.*\}", text, re.S)
        if match:
            return json.loads(match.group())
    except:
        pass
    return {}


# ==============================
# AI Agent Extraction
# ==============================

def ai_agent_extract(image_path):

    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="Qwen/Qwen3-VL-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=400,
    )

    try:
        content = response.choices[0].message.content
    except:
        content = str(response)

    extracted_fields = extract_json(content)

    return extracted_fields
