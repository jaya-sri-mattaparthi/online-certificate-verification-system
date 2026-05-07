import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. CONFIGURATION (AWS Template Calibration)
# ==========================================
TEMPLATE_PATH = "aws_template.png"
OUTPUT_DIR = "AWS_Certificates"

# UNIFIED FONT STYLE
FONT_STYLE = r"C:\Windows\Fonts\arialbd.ttf"

# TEXT SIZES
NAME_SIZE = 30
COURSE_SIZE = 30
SERIAL_SIZE = 30

# COORDINATES
NAME_X, NAME_Y = 150, 350
COURSE_X, COURSE_Y = 150, 480
SERIAL_X, SERIAL_Y = 1100, 830

# COLORS (Matched to AWS Charcoal Grey)
TEXT_COLOR = (35, 31, 32)

# ==========================================
# 2. 150 UNIQUE NAMES (Divided by AWS Course)
# ==========================================
architect_names = [
    "Liam Smith", "Olivia Johnson", "Noah Williams", "Emma Brown", "Oliver Jones", "Ava Garcia", "Elijah Miller", "Sophia Davis", "James Rodriguez", "Isabella Martinez", "William Hernandez", "Mia Lopez",
    "Benjamin Gonzalez", "Charlotte Wilson", "Lucas Anderson", "Amelia Thomas", "Henry Taylor", "Evelyn Moore", "Theodore Jackson", "Abigail Martin", "Alexander Lee", "Harper Perez", "Jackson Thompson",
    "Emily White", "Sebastian Harris", "Elizabeth Sanchez", "Mateo Clark", "Avery Ramirez", "Samuel Lewis", "Sofia Robinson", "David Walker", "Ella Young", "Joseph Allen", "Madison King", "Carter Wright",
    "Scarlett Scott", "Owen Torres", "Victoria Nguyen", "Wyatt Hill", "Aria Flores", "John Green", "Grace Adams", "Jack Nelson", "Chloe Baker", "Luke Hall", "Camila Rivera", "Jayden Campbell", "Penelope Mitchell", "Dylan Carter", "Riley Roberts", "Isaac Gomez"
]

practitioner_names = [
    "Layla Phillips", "Gabriel Evans", "Lillian Turner", "Julian Diaz", "Nora Parker", "Levi Cruz", "Zoey Edwards", "Anthony Collins", "Mila Reyes",
    "Grayson Stewart", "Aubrey Morris", "Christopher Morales", "Hannah Murphy", "Joshua Cook", "Lily Rogers", "Andrew Gutierrez", "Addison Ortiz", "Lincoln Morgan", "Eleanor Cooper", "Mateo Peterson",
    "Natalie Bailey", "Ryan Reed", "Luna Kelly", "Jaxon Howard", "Savannah Ramos", "Nathan Kim", "Brooklyn Cox", "Aaron Ward", "Zoe Richardson", "Isaiah Watson", "Stella Brooks", "Thomas Chao", "Hazel Wood",
    "Charles James", "Ellie Bennett", "Caleb Gray", "Paisley Mendoza", "Josiah Ruiz", "Audrey Hughes", "Christian Price", "Skylar Alvarez", "Hunter Castillo", "Violet Sanders", "Eli Patel", "Claire Myers",
    "Jonathan Long", "Bella Ross", "Connor Foster", "Aurora Jimenez"
]

dataset = {
    "AWS Cloud Solutions Architect": architect_names,
    "AWS Certified Cloud Practitioner": practitioner_names,
}

# ==========================================
# 3. GENERATION ENGINE
# ==========================================
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_aws_dataset():
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: {TEMPLATE_PATH} not found.")
        return

    img_template = Image.open(TEMPLATE_PATH)
    global_counter = 1

    for course_title, name_list in dataset.items():
        print(f"\nGenerating for Course: {course_title}")

        for name in name_list:
            # Create fresh RGB copy
            img = img_template.copy().convert("RGB")
            draw = ImageDraw.Draw(img)

            # Load Fonts
            name_f = ImageFont.truetype(FONT_STYLE, NAME_SIZE)
            course_f = ImageFont.truetype(FONT_STYLE, COURSE_SIZE)
            serial_f = ImageFont.truetype(FONT_STYLE, SERIAL_SIZE)

            # Draw the unique Student Name
            draw.text((NAME_X, NAME_Y), name, fill=TEXT_COLOR, font=name_f)

            # Draw the specific Course Title
            draw.text((COURSE_X, COURSE_Y), course_title,
                      fill=TEXT_COLOR, font=course_f)

            # Define Serial ID and draw Text
            serial_id = f"A{global_counter+100:03d}"
            serial_text = f"Serial No: {serial_id}"
            draw.text((SERIAL_X, SERIAL_Y), serial_text,
                      fill=TEXT_COLOR, font=serial_f)

            # Save result - File named by the Serial ID (e.g., A001.jpg)
            file_name = f"{serial_id}.jpg"
            img.save(os.path.join(OUTPUT_DIR, file_name), "JPEG", quality=95)

            global_counter += 1

    print(
        f"\nTask Complete! Files saved in '{OUTPUT_DIR}' named by Serial No.")


if __name__ == "__main__":
    generate_aws_dataset()
