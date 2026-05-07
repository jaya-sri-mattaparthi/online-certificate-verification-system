import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. CONFIGURATION (AWS Template Calibration)
# ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "upgrad.png")
OUTPUT_DIR = "Upgrad_Certificates"

# UNIFIED FONT STYLE
FONT_STYLE = r"C:\Windows\Fonts\arialbd.ttf"

# TEXT SIZES
NAME_SIZE = 30
COURSE_SIZE = 30
SERIAL_SIZE = 30

# COORDINATES
NAME_X, NAME_Y = 660, 290
COURSE_X, COURSE_Y = 620, 425
SERIAL_X, SERIAL_Y = 1200, 910

# COLORS (Matched to AWS Charcoal Grey)
TEXT_COLOR = (35, 31, 32)

# ==========================================
# 2. 150 UNIQUE NAMES (Divided by AWS Course)
# ==========================================
android_names = [
    "Nihal Nguyen", "Okda Hill", "Phact Flores", "Rigel Green", "Sirius Adams", "Talitha Nelson",
    "Unukalhai Baker", "Vega Hall", "Wasat Rivera", "Xylia Campbell", "Yed Mitchell", "Zaurak Carter", "Acamar Roberts", "Beid Gomez", "Castor Phillips", "Diphda Evans", "Edasich Turner",
    "Furud Diaz", "Gienah Parker", "Homam Cruz", "Imai Edwards", "Jih Collins", "Kraz Reyes", "Lilii Stewart", "Mebsuta Morris", "Nihal Morales", "Okda Murphy", "Phact Cook", "Rigel Rogers", "Sirius Gutierrez",
    "Talitha Ortiz", "Unukalhai Morgan", "Vega Cooper", "Wasat Peterson", "Xylia Bailey", "Yed Reed", "Zaurak Kelly", "Acamar Howard", "Beid Ramos", "Castor Kim", "Diphda Cox", "Edasich Ward", "Furud Richardson",
    "Gienah Watson", "Homam Brooks", "Imai Chao", "Jih Wood", "Kraz James", "Lilii Bennett", "Mebsuta Gray", "Nihal Mendoza", "Okda Ruiz", "Phact Hughes", "Rigel Price", "Sirius Alvarez", "Talitha Castillo",
    "Unukalhai Sanders", "Vega Patel", "Wasat Myers", "Xylia Long", "Yed Ross", "Zaurak Foster", "Acamar Jimenez", "Beid Helios", "Castor Washington", "Diphda Butler", "Edasich Simmons", "Furud Foster",
    "Gienah Jimenez", "Homam Gonzales", "Imai Bryant", "Jih Alexander", "Kraz Russell", "Lilii Griffin", "Mebsuta Diaz", "Nihal Hayes", "Okda Myers", "Phact Ford", "Rigel Hamilton", "Sirius Graham",
    "Talitha Sullivan", "Unukalhai Wallace", "Vega Cole", "Wasat West", "Xylia Jordan", "Yed Owens", "Zaurak Reynolds", "Acamar Fisher", "Beid Ellis", "Castor Harrison", "Diphda Gibson",
    "Edasich Mcdonald", "Furud Cruz", "Gienah Marshall", "Homam Ortiz", "Imai Gomez", "Jih Murray", "Kraz Freeman", "Lilii Wells", "Mebsuta Webb", "Nihal Simpson", "Okda Stevens", "Phact Tucker",
    "Rigel Porter", "Sirius Hunter", "Talitha Hicks", "Unukalhai Crawford", "Vega Henry", "Wasat Boyd", "Xylia Mason", "Yed Morales", "Zaurak Kennedy", "Acamar Warren", "Beid Dixon", "Castor Ramos", "Diphda Reyes",
    "Edasich Burns", "Furud Gordon", "Gienah Shaw", "Homam Holmes", "Imai Rice", "Jih Robertson", "Kraz Hunt", "Lilii Black", "Mebsuta Daniels", "Nihal Palmer", "Okda Mills", "Phact Nichols", "Rigel Grant",
    "Sirius Knight", "Talitha Ferguson", "Unukalhai Rose", "Vega Stone", "Wasat Hawkins", "Xylia Dunn", "Yed Perkins", "Zaurak Hudson", "Acamar Spencer", "Beid Gardner", "Castor Stephens", "Diphda Payne",
    "Edasich Pierce", "Furud Berry", "Gienah Matthews", "Homam Arnold", "Imai Wagner", "Jih Willis", "Kraz Ray", "Lilii Watkins", "Mebsuta Olson", "Nihal Carroll", "Okda Duncan", "Phact Snyder", "Rigel Hart",
    "Sirius Cunningham", "Talitha Bradley", "Unukalhai Lane", "Vega Andrews", "Wasat Ruiz", "Xylia Harper", "Yed Fox", "Zaurak Riley", "Acamar Armstrong", "Beid Carpenter", "Castor Weaver", "Diphda Greene",
    "Edasich Lawrence", "Furud Elliott", "Gienah Chavez", "Homam Wyatt", "Imai Li", "Jih Wang", "Kraz Kim", "Lilii Nguyen", "Mebsuta Gupta", "Nihal Kumar", "Okda Singh", "Phact Sato", "Rigel Tanaka",
    "Sirius Suzuki", "Talitha Takahashi", "Unukalhai Ito", "Vega Watanabe", "Wasat Nakamura", "Xylia Kobayashi", "Yed Kato", "Zaurak Yoshida", "Acamar Yamada", "Beid Sasaki", "Castor Yamaguchi",
    "Diphda Saito", "Edasich Matsumoto", "Furud Inoue", "Gienah Kimura", "Homam Hayashi", "Imai Shimizu", "Jih Yamazaki", "Kraz Mori", "Lilii Abe", "Mebsuta Ikeda", "Nihal Hashimoto", "Okda Yamashita",
    "Phact Ishikawa", "Rigel Maeda", "Sirius Fujita", "Talitha Okada", "Unukalhai Goto", "Vega Hasegawa", "Wasat Murakami", "Xylia Kondo", "Yed Sakamoto", "Zaurak Endo", "Acamar Aoki", "Beid Fujii",
    "Castor Nishimura", "Diphda Fujiwara", "Edasich Miura", "Furud Okamoto", "Gienah Matsuda", "Homam Nakagawa", "Imai Nakano", "Jih Matsui", "Kraz Kojima", "Lilii Hara", "Mebsuta Wada", "Nihal Kaneko",
    "Okda Tamura", "Phact Taniguchi", "Rigel Ono", "Sirius Nakajima", "Talitha Ueda", "Unukalhai Matsuo", "Vega Kikuchi", "Wasat Sugiyama", "Xylia Takeda", "Yed Arai", "Zaurak Hirano", "Acamar Noguchi",
    "Beid Sugimoto", "Castor Chiba", "Diphda Nomura", "Edasich Kudo", "Furud Sano", "Gienah Sugawara", "Homam Kubo", "Imai Matsuura", "Jih Kinoshita", "Kraz Iwasaki", "Lilii Noguchi", "Mebsuta Koyama", "Nihal Onishi",
    "Okda Takagi", "Phact Baba", "Rigel Fukuda", "Sirius Matsumoto", "Talitha Shima", "Unukalhai Tanabe", "Vega Matsumura", "Wasat Sawada", "Xylia Ota", "Yed Horie", "Zaurak Seki", "Acamar Imai", "Beid Uchida",
    "Castor Yokoyama", "Diphda Shimada", "Edasich Yamauchi", "Furud Nakano", "Gienah Masuda", "Homam Katayama", "Imai Okazaki", "Jih Hirai", "Kraz Noda", "Lilii Koga", "Mebsuta Otsuka", "Nihal Kawano", "Okda Tajima",
    "Phact Kamata", "Rigel Shibuya", "Sirius Mizuno", "Talitha Kishimoto", "Unukalhai Numata", "Vega Tsuji", "Wasat Inaba", "Xylia Okumura", "Yed Kawaguchi", "Zaurak Shiraishi", "Acamar Miyake", "Beid Kitamura",
    "Castor Kurata", "Diphda Shinohara", "Edasich Asano", "Furud Tani", "Gienah Hata", "Homam Irie", "Imai Toyoda", "Jih Kanda", "Kraz Nagai", "Lilii Oki", "Mebsuta Komatsu",
]

blockchain_names = [
    "Nihal Matsushima", "Okda Ikeuchi",
    "Phact Sugita", "Rigel Ozawa", "Sirius Shinozaki", "Talitha Yoshioka", "Unukalhai Kuroda", "Vega Kase", "Wasat Kawashima", "Xylia Tsuchiya", "Yed Fukui", "Zaurak Nanbu", "Acamar Arima", "Beid Ishida",
    "Castor Kumagai", "Diphda Shima", "Edasich Tokunaga", "Furud Kasai", "Gienah Yanagi", "Homam Omori", "Imai Takei", "Jih Yasuda", "Kraz Murata", "Lilii Hagiwara", "Mebsuta Bessho", "Nihal Oishi", "Okda Kawahara",
    "Phact Sudo", "Rigel Hirayama", "Sirius Ogura", "Talitha Nagasawa", "Unukalhai Kodama", "Vega Hirasawa", "Wasat Kawada", "Xylia Katsura", "Yed Enomoto", "Zaurak Tottori", "Acamar Shiina", "Beid Nakatani",
    "Castor Terada", "Diphda Sugawara", "Edasich Shibazaki", "Furud Akimoto", "Gienah Mitsui", "Homam Tsuru", "Imai Shino", "Jih Kitano", "Kraz Niwa", "Lilii Shiro", "Mebsuta Hoshino", "Nihal Koyama",
    "Okda Kanemoto", "Phact Higo", "Rigel Arima", "Sirius Mogi", "Talitha Koshino", "Unukalhai Shiota", "Vega Inoue", "Wasat Tsuda", "Xylia Serizawa", "Yed Okuma", "Zaurak Shirai", "Acamar Kanda",
    "Beid Horikoshi", "Castor Sawa", "Diphda Ohara", "Edasich Ebara", "Furud Maki", "Gienah Sugino", "Homam Shima", "Imai Taira", "Jih Eguchi", "Kraz Higa", "Lilii Shima", "Mebsuta Gushiken", "Nihal Shima",
    "Okda Uehara", "Phact Tamaki", "Rigel Kina", "Sirius Miyashiro", "Talitha Yonamine", "Unukalhai Shimabukuro", "Vega Teruya", "Wasat Arakaki", "Xylia Oshiro", "Yed Shima", "Zaurak Shima",
    "Aaliyah Smith", "Aaron Johnson", "Abel Williams", "Abigail Brown", "Abraham Jones", "Ada Garcia", "Adaline Miller", "Adalyn Davis", "Adam Rodriguez", "Addison Martinez", "Adeline Hernandez", "Adelyn Lopez",
    "Aden Gonzalez", "Aditya Wilson", "Adolfo Anderson", "Adonis Thomas", "Adrian Taylor", "Adriana Moore", "Adrianna Jackson", "Adriel Martin", "Adrien Lee", "Adrienne Perez", "Afton Thompson", "Agatha White",
    "Agustin Harris", "Ahmad Sanchez", "Ahmed Clark", "Aida Ramirez", "Aidan Lewis", "Aiden Robinson", "Aiko Walker", "Aileen Young", "Ailsa Allen", "Aimee King", "Ainsley Wright", "Aisha Scott", "Aiyana Torres",
    "Aja Nguyen", "Akira Hill", "Al Flores", "Alaina Green", "Alan Adams", "Alana Nelson", "Alani Baker", "Alannah Hall", "Alaya Rivera", "Alayna Campbell", "Alba Mitchell", "Albert Carter", "Alberta Roberts",
    "Alberto Gomez", "Albin Phillips", "Alden Evans", "Aldo Turner", "Aleah Diaz", "Alec Parker", "Alecia Cruz", "Alejandra Edwards", "Alejandro Collins", "Alena Reyes", "Alessandra Stewart", "Alessandro Morris",
    "Alessia Morales", "Alex Murphy", "Alexa Cook", "Alexander Rogers", "Alexandra Gutierrez", "Alexandria Ortiz", "Alexandro Morgan", "Alexia Cooper", "Alexis Peterson", "Alexus Bailey", "Alfonso Reed",
    "Alfred Kelly", "Alfredo Howard", "Ali Ramos", "Alia Kim", "Alice Cox", "Alicia Ward", "Alijah Richardson", "Alina Watson", "Alisa Brooks", "Alisha Chao", "Alison Wood", "Alissa James",
    "Alivia Bennett", "Alix Gray", "Aliya Mendoza", "Aliyah Ruiz", "Alize Hughes", "Allan Price", "Allen Alvarez", "Allie Castillo", "Allison Sanders", "Allyson Patel", "Alma Myers", "Alondra Long",
    "Alonso Ross", "Alonzo Foster", "Alphonso Jimenez", "Althea Helios", "Alvaro Washington", "Alvin Butler", "Alyson Simmons", "Alyssa Foster", "Amara Jimenez", "Amari Gonzales", "Amaris Bryant", "Amaya Alexander",
    "Amber Russell", "Amelia Griffin", "Amelie Diaz", "America Hayes", "Americus Myers", "Amery Ford", "Ami Hamilton", "Amia Graham", "Amie Sullivan", "Amir Wallace", "Amira Cole", "Amity West", "Amos Jordan",
    "Amy Owens", "Amya Reynolds", "Ana Fisher", "Anabel Ellis", "Anabella Harrison", "Anabelle Gibson", "Anahi Mcdonald", "Anais Cruz", "Analia Marshall", "Anastasia Ortiz", "Anaya Gomez", "Anders Murray",
    "Anderson Freeman", "Andre Wells", "Andrea Webb", "Andreas Simpson", "Andres Stevens", "Andrew Tucker", "Andria Porter", "Androula Hunter", "Andy Hicks", "Angel Crawford", "Angela Henry", "Angelia Boyd",
    "Angelica Mason", "Angelina Morales", "Angeline Kennedy", "Angelique Warren", "Angelo Dixon", "Angie Ramos", "Angus Reyes", "Anika Burns", "Anisa Gordon", "Aniya Shaw", "Aniyah Holmes", "Anjali Rice",
    "Ann Robertson", "Anna Hunt", "Annabel Black", "Annabella Daniels", "Annabelle Palmer", "Annalise Mills", "Anne Nichols", "Annette Grant", "Annie Knight", "Annika Ferguson", "Annmarie Rose", "Ansel Stone",
    "Anson Hawkins", "Anthony Dunn", "Antoinette Perkins", "Anton Hudson", "Antonia Spencer", "Antonio Gardner", "Antony Stephens", "Antwan Payne", "Anya Pierce", "Apollo Berry", "April Matthews",
    "Arabella Arnold", "Araceli Wagner", "Aracely Willis", "Archer Ray", "Archie Watkins", "Ardith Olson", "Arely Carroll", "Ares Duncan", "Aretina Snyder", "Aria Hart", "Ariana Cunningham", "Ariane Bradley",
    "Arianna Lane", "Ariel Andrews", "Ariella Ruiz", "Arielle Harper", "Arjun Fox", "Arleen Riley", "Arlene Armstrong", "Arlo Carpenter", "Armando Weaver", "Armani Greene", "Arnaldo Lawrence", "Arnav Elliott",
    "Arnie Chavez", "Arnold Wyatt", "Aron Li", "Arthur Wang", "Arturo Kim", "Arun Nguyen", "Arvella Gupta", "Arvid Kumar"
]

dataset = {
    "Android Development": android_names,
    "Blockchain Development": blockchain_names,
}

# ==========================================
# 3. GENERATION ENGINE
# ==========================================
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_upgrad_dataset():
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
            serial_id = f"P{global_counter:03d}"
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
    generate_upgrad_dataset()
