import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. CONFIGURATION (Google Template)
# ==========================================
TEMPLATE_PATH = "google_template.png"
OUTPUT_DIR = "Google_Certificates"

FONT_STYLE = r"C:\Windows\Fonts\arialbd.ttf"
NAME_SIZE, COURSE_SIZE, SERIAL_SIZE = 30, 30, 30
NAME_X, NAME_Y = 140, 380
COURSE_X, COURSE_Y = 140, 530
SERIAL_X, SERIAL_Y = 1100, 880
TEXT_COLOR = (35, 31, 32)

# ==========================================
# 2. UNIQUE NAMES (Common Indian Names)
# ==========================================
ux_names = [
    "Landon Helios", "Lucy Washington", "Adrian Butler", "Anna Simmons", "Asher Foster", "Samantha Jimenez", "Cameron Gonzales", "Caroline Bryant", "Leo Alexander", "Genesis Russell", "Hunter Griffin", "Aaliyah Diaz", "Jeremiah Hayes", "Kennedy Myers", "Zander Ford", "Kinsley Hamilton", "Jordan Graham", "Allison Sullivan", "Ian Wallace", "Maya Cole", "Elias West", "Madelyn Jordan", "Caleb Owens", "Adeline Reynolds", "Nolan Fisher", "Alexa Ellis", "Brooks Harrison", "Ariana Gibson", "Robert Mcdonald", "Elena Cruz",
    "Angel Marshall", "Gabriella Ortiz", "Waylon Gomez", "Alice Murray", "Jameson Freeman", "Sadie Wells", "Santiago Webb", "Sophie Simpson", "Axel Stevens", "Hailey Tucker", "Cooper Porter", "Eva Hunter",
    "Roman Hicks", "Emilia Crawford", "Xavier Henry", "Autumn Boyd", "Kai Mason", "Quinn Morales", "Sawyer Kennedy", "Nevaeh Warren"
]

data_names = [
    "Everett Dixon", "Piper Ramos", "Miles Reyes", "Ruby Burns",
    "Parker Gordon", "Serenity Shaw", "Wesley Holmes", "Willow Rice", "Jason Robertson", "Everly Hunt", "Declan Black", "Cora Daniels", "Bennett Palmer", "Kaylee Mills", "Silas Nichols", "Lydia Grant",
    "Damian Knight", "Aubree Ferguson", "Micah Rose", "Arianna Stone", "Arlo Hawkins", "Eliana Dunn", "Luca Perkins", "Peyton Hudson", "Ezekiel Spencer", "Melanie Gardner", "George Stephens",
    "Gianna Payne", "Amir Pierce", "Isabelle Berry", "Victor Matthews", "Julia Arnold", "Rowan Wagner", "Valentina Willis", "Gael Ray", "Clara Watkins", "Harrison Olson", "Vivian Carroll",
    "Braxton Duncan", "Delilah Snyder", "Ryder Hart", "Raelynn Cunningham", "Maxwell Bradley", "Natalia Lane", "Brandon Andrews", "Jade Ruiz", "Kevin Harper", "Iris Fox", "Justin Riley", "Athena Armstrong"
]

dataset = {
    "Google UX Design": ux_names,
    "Google Data Analytics": data_names,
}

# ==========================================
# 3. GENERATION ENGINE
# ==========================================
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_full_dataset():
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: {TEMPLATE_PATH} not found.")
        return

    img_template = Image.open(TEMPLATE_PATH)
    global_counter = 1

    for course_title, name_list in dataset.items():
        print(f"\nStarting generation for: {course_title}")

        for name in name_list:
            img = img_template.copy().convert("RGB")
            draw = ImageDraw.Draw(img)

            # Fonts with specific sizes
            name_f = ImageFont.truetype(FONT_STYLE, NAME_SIZE)
            course_f = ImageFont.truetype(FONT_STYLE, COURSE_SIZE)
            serial_f = ImageFont.truetype(FONT_STYLE, SERIAL_SIZE)

            # Draw Elements
            draw.text((NAME_X, NAME_Y), name, fill=TEXT_COLOR, font=name_f)
            draw.text((COURSE_X, COURSE_Y), course_title,
                      fill=TEXT_COLOR, font=course_f)

            # Define Serial ID (Prefix G for Google)
            serial_id = f"G{global_counter + 100:03d}"
            serial_text = f"Serial No: {serial_id}"
            draw.text((SERIAL_X, SERIAL_Y), serial_text,
                      fill=TEXT_COLOR, font=serial_f)

            # Save file named by Serial ID
            file_name = f"{serial_id}.jpg"
            img.save(os.path.join(OUTPUT_DIR, file_name), "JPEG", quality=95)

            global_counter += 1

    print(
        f"\nSuccess! Certificates generated in '{OUTPUT_DIR}' named by Serial No.")


if __name__ == "__main__":
    generate_full_dataset()
