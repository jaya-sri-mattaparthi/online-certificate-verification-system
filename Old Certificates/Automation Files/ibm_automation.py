import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. CONFIGURATION (Google Template)
# ==========================================
TEMPLATE_PATH = "ibm_template.png"
OUTPUT_DIR = "IBM_Certificates"

FONT_STYLE = r"C:\Windows\Fonts\arialbd.ttf"
NAME_SIZE, COURSE_SIZE, SERIAL_SIZE = 30, 30, 30
NAME_X, NAME_Y = 150, 380
COURSE_X, COURSE_Y = 150, 530
SERIAL_X, SERIAL_Y = 1100, 890
TEXT_COLOR = (35, 31, 32)

# ==========================================
# 2. UNIQUE NAMES (Common Indian Names)
# ==========================================
data_science_names = [
    "George Carpenter", "Mariah Weaver", "Abel Greene", "Hope Lawrence", "Zion Elliott", "Lola Chavez", "Milo Wyatt", "Lucia Li", "Zachary Wang", "Esther Kim", "Tyler Nguyen", "Rose Gupta",
    "Elliott Kumar", "Brielle Singh", "Alan Sato", "Adalynn Tanaka", "Nicholas Suzuki", "Rylee Takahashi", "Judah Ito", "Desiree Watanabe", "Ivan Nakamura", "Sloane Kobayashi", "Malachi Kato",
    "Leilani Yoshida", "Beckett Yamada", "Kaitlyn Sasaki", "Jasper Yamaguchi", "Freya Saito", "Emmanuel Matsumoto", "Amara Inoue", "Abraham Kimura", "Daisy Hayashi", "Jesse Shimizu", "Harmony Yamazaki",
    "Lorenzo Mori", "Sasha Abe", "Arthur Ikeda", "Alani Hashimoto", "Leon Yamashita", "Elise Ishikawa", "Felix Maeda", "Alana Fujita", "Dean Okada", "Sienna Goto", "Holden Hasegawa", "Ari Murakami", "Gideon Kondo",
    "Makenzie Sakamoto", "River Endo", "Lia Aoki"
]

python_names = [
    "Kaleb Fujii", "Lucille Nishimura", "Emmett Fujiwara", "Daphne Miura", "Louis Okamoto", "Miriam Matsuda", "Tucker Nakagawa", "Nadia Nakano", "Walker Matsui",
    "Celia Kojima", "Kobe Hara", "Kiara Wada", "Lane Kaneko", "Tessa Tamura", "Beckham Taniguchi", "Sutton Ono", "Reed Nakajima", "Maliyah Ueda", "Seth Matsuo", "Kyla Kikuchi", "Barrett Sugiyama",
    "Noelle Takeda", "Paxton Arai", "Gemma Hirano", "Stephen Noguchi", "Adelaide Sugimoto", "Callum Chiba", "Daleyza Nomura", "Lukas Kudo", "Journee Sano", "Dante Sugawara", "Ivory Kubo", "Tobias Matsuura",
    "Ayla Kinoshita", "Arlo Iwasaki", "Kailani Noguchi", "Forrest Koyama", "Willa Onishi", "Ismael Takagi", "Lorelai Baba", "Zayn Fukuda", "Mina Matsumoto", "Kade Shima", "Selena Tanabe", "Romeo Matsumura",
    "Esme Sawada", "Zaire Ota", "Harlow Horie", "Kase Seki", "Kyra Imai"
]

dataset = {
    "Introduction to Data Science": data_science_names,
    "Python Development": python_names,
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
            serial_id = f"I{global_counter + 100:03d}"
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
