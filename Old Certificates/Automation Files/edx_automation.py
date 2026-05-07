import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. CONFIGURATION (AWS Template Calibration)
# ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "edx.png")
OUTPUT_DIR = "Edx_Certificates"

# UNIFIED FONT STYLE
FONT_STYLE = r"C:\Windows\Fonts\arialbd.ttf"

# TEXT SIZES
NAME_SIZE = 30
COURSE_SIZE = 30
SERIAL_SIZE = 30

# COORDINATES
NAME_X, NAME_Y = 100, 370
COURSE_X, COURSE_Y = 100, 500
SERIAL_X, SERIAL_Y = 1250, 950

# COLORS (Matched to AWS Charcoal Grey)
TEXT_COLOR = (35, 31, 32)

# ==========================================
# 2. 150 UNIQUE NAMES (Divided by AWS Course)
# ==========================================
python_names = [
    "Daxton Uchida", "Dream Yokoyama", "Kayson Shimada", "Hattie Yamauchi", "Milan Nakano", "Nola Masuda", "Cyrus Katayama", "Rosalie Okazaki",
    "Enzo Hirai", "Legacy Noda", "Kellan Koga", "Tatum Otsuka", "Princeton Kawano", "Myra Tajima", "Omari Kamata", "Sariyah Shibuya", "Ronan Mizuno", "Zaniyah Kishimoto", "Kaysen Numata", "Yareli Tsuji",
    "Ari Inaba", "Rayna Okumura", "Nikolai Kawaguchi", "Bria Shiraishi", "Wilder Miyake", "Alia Kitamura", "Sincere Kurata", "Estella Shinohara", "Kendrick Asano", "Bailee Tani", "Raiden Hata", "Zariah Irie",
    "Eno Toyoda", "Amani Kanda", "Benson Nagai", "Aniyah Oki", "Koda Komatsu", "Miah Matsushima", "Memphis Ikeuchi", "Hester Sugita", "Kiaan Ozawa", "Lyra Shinozaki", "Mordechai Yoshioka", "Kairi Kuroda",
    "Winston Kase", "Sarai Kawashima", "Zev Tsuchiya", "Zora Fukui", "Alistair Nanbu", "Aurelia Arima", "Bo Ishida", "Hollis Kumagai", "Cassius Shima", "Ila Tokunaga", "Cillian Kasai", "Inaya Yanagi",
    "Grey Omori", "Jovie Takei", "Hezekiah Yasuda", "Kahlani Murata", "Jericho Hagiwara", "Lianna Bessho", "Kye Oishi", "Marlowe Kawahara", "Ledger Sudo", "Mavis Hirayama", "Mccoy Ogura", "Neriah Nagasawa",
    "Niklaus Kodama", "Nyra Hirasawa", "Onyx Kawada", "Paloma Katsura", "Rayden Enomoto", "Rhea Tottori", "Saint Shiina", "Sia Nakatani", "Seven Terada", "Tinsley Sugawara", "Vance Shibazaki", "Zayla Akimoto",
    "Ziya Mitsui", "Axl Tsuru", "Bellamy Shino", "Crosby Kitano", "Elowen Niwa", "Fisher Shiro", "Goldie Hoshino", "Huxley Koyama", "Indie Kanemoto", "Jagger Higo", "Kaya Arima", "Loyal Mogi", "Moon Koshino",
    "Nixon Shiota", "Oakley Inoue", "Perry Tsuda", "Quincy Serizawa", "Rogue Okuma", "Sunny Shirai", "True Kanda", "Ulysses Horikoshi", "Veda Sawa", "Wells Ohara", "Xyla Ebara", "Yosef Maki", "Zola Sugino",
    "Aditya Shima", "Bastien Taira", "Calliope Eguchi", "Dorian Higa", "Etta Shima", "Flynn Gushiken", "Gaia Shima", "Hale Uehara", "Ida Tamaki", "Juno Kina", "Kit Miyashiro", "Lark Yonamine",
    "Musa Shimabukuro", "Nyx Teruya", "Ozzie Arakaki", "Pia Oshiro", "Rhodes Shima", "Soren Shima", "Thais Shima", "Uri Shima", "Vita Shima", "Wolf Shima", "Xena Shima", "Yael Shima", "Zeke Shima",
    "Abner Smith", "Beulah Johnson", "Cletus Williams", "Dovie Brown", "Elmo Jones", "Fannie Garcia", "Grover Miller", "Hester Davis", "Ira Rodriguez", "Jannie Martinez", "Kermit Hernandez", "Lovie Lopez", "Milton Gonzalez", "Nannie Wilson", "Odis Anderson", "Pansie Thomas", "Quinton Taylor", "Roxie Moore", "Selmer Jackson", "Tillie Martin", "Ursula Lee", "Vester Perez", "Winnie Thompson", "Xavion White",
    "Yula Harris", "Zebulon Sanchez", "Agatha Clark", "Barnaby Ramirez", "Cecily Lewis", "Dudley Robinson", "Euphemia Walker", "Ferdinand Young", "Gwenyth Allen", "Humphrey King", "Isadora Wright",
    "Jedidiah Scott", "Keziah Torres", "Leander Nguyen", "Minerva Hill", "Nathanael Flores", "Obadiah Green", "Prudence Adams", "Quintin Nelson", "Rosalind Baker", "Simeon Hall", "Tabitha Rivera", "Uriel Campbell",
    "Verity Mitchell", "Wilfred Carter", "Xenia Roberts", "Yadriel Gomez", "Zenobia Phillips", "Amon Evans", "Beryl Turner", "Cyprian Diaz", "Dymphna Parker", "Ephraim Cruz", "Flavia Edwards", "Gideon Collins",
    "Hilda Reyes", "Ignatius Stewart", "Jessamine Morris", "Konrad Morales", "Leona Murphy", "Magnus Cook", "Nona Rogers", "Oswald Gutierrez", "Phyllis Ortiz", "Quentin Morgan", "Rowena Cooper", "Swithin Peterson",
    "Theodora Bailey", "Urban Reed", "Valerius Kelly", "Winifred Howard", "Xerxes Ramos", "Yolanda Kim", "Zadok Cox", "Amity Ward", "Basil Richardson", "Clarissa Watson", "Desmond Brooks", "Eulalia Chao",
    "Fitzgerald Wood", "Genevieve James", "Horatio Bennett", "Idonia Gray", "Jolyon Mendoza", "Kasmira Ruiz", "Lysander Hughes", "Millicent Price", "Neville Alvarez", "Octavia Castillo", "Percival Sanders",
    "Quintessa Patel", "Roderick Myers", "Sybil Long", "Theobald Ross", "Ursula Foster", "Valentine Jimenez", "Wallis Helios", "Xaveria Washington", "Yeardley Butler", "Zosimus Simmons", "Anselm Foster",
    "Beatrix Jimenez", "Caspar Gonzales", "Dorothea Bryant", "Eustace Alexander", "Felicity Russell", "Gawain Griffin", "Honoria Diaz", "Ivor Hayes", "Jacinta Myers", "Kyros Ford", "Lucinda Hamilton",
    "Marmaduke Graham", "Nephele Sullivan", "Orpheus Wallace", "Parthenia Cole", "Raban West", "Sabina Jordan", "Tadhg Owens", "Ulyssa Reynolds", "Viggo Fisher", "Wilhelmina Ellis", "Xanthus Harrison", "Yseult Gibson",
    "Zoticus Mcdonald", "Ariadne Cruz", "Balthazar Marshall", "Cosima Ortiz", "Diodorus Gomez", "Euphemia Murray", "Fabian Freeman", "Gorgonia Wells", "Hesperos Webb", "Iphigenia Simpson", "Justinian Stevens",
    "Kyriake Tucker", "Leontius Porter", "Melanthios Hunter", "Nikephoros Hicks", "Olympias Crawford", "Pancratius Henry", "Roxane Boyd", "Sophronia Mason", "Theophanes Morales", "Uranie Kennedy",
    "Valerius Warren", "Xenophon Dixon", "Yorgos Ramos", "Zosime Reyes", "Aegidius Burns", "Blandina Gordon", "Caelestinus Shaw", "Donatella Holmes", "Evaristus Rice", "Faustina Robertson", "Gelasius Hunt",
    "Hilarion Black", "Irenaeus Daniels", "Jovinianus Palmer", "Kyriakos Mills", "Laurentius Nichols", "Marciana Grant", "Nereus Knight", "Onesimus Ferguson", "Polycarpus Rose"
]

ml_names = [
    "Quodvultdeus Stone", "Romedius Hawkins", "Spyridon Dunn", "Telesphorus Perkins", "Ursicinus Hudson", "Vitalianus Spencer", "Wiborada Gardner", "Xystus Stephens", "Yared Payne", "Zoticus Pierce", "Ambrose Berry",
    "Boniface Matthews", "Cyprian Arnold", "Dionysius Wagner", "Erasmus Willis", "Fulgentius Ray", "Gregory Watkins", "Hyacinth Olson", "Isidore Carroll", "Jerome Duncan", "Kunigunde Snyder", "Lambert Hart",
    "Methodius Cunningham", "Norbert Bradley", "Odo Lane", "Pancras Andrews", "Quintus Ruiz", "Remigius Harper", "Servatius Fox", "Tarcisius Riley", "Ulric Armstrong", "Vitus Carpenter", "Wenceslaus Weaver",
    "Xavier Greene", "Yvo Lawrence", "Zeno Elliott", "Anatole Chavez", "Blaise Wyatt", "Cletus Li", "Damasus Wang", "Eusebius Kim", "Fabius Nguyen", "Gratian Gupta", "Hermes Kumar", "Innocent Singh",
    "Januarius Sato", "Linus Tanaka", "Marius Suzuki", "Nicodemus Takahashi", "Optatus Ito", "Pontius Watanabe", "Quirinus Nakamura", "Rufus Kobayashi", "Sixtus Kato", "Titus Yoshida", "Urbanus Yamada",
    "Valerian Sasaki", "Xavier Yamaguchi", "Yuli Saito", "Zoticus Matsumoto", "Artemis Inoue", "Boreas Kimura", "Chloris Hayashi", "Doris Shimizu", "Eros Yamazaki", "Flora Mori", "Gaia Abe", "Helios Ikeda",
    "Iris Hashimoto", "Janus Yamashita", "Khione Ishikawa", "Leto Maeda", "Morpheus Fujita", "Nyx Okada", "Oceanus Goto", "Phoebe Hasegawa", "Quirinus Murakami", "Rhea Kondo", "Selene Sakamoto", "Thalassa Endo",
    "Uranus Aoki", "Vesper Fujii", "Zephyrus Nishimura", "Astra Fujiwara", "Bruma Miura", "Caelum Okamoto", "Dies Matsuda", "Eurus Nakagawa", "Favonius Nakano", "Glaucus Matsui", "Horae Kojima", "Ignis Hara",
    "Juno Wada", "Keres Kaneko", "Luna Tamura", "Metis Taniguchi", "Nox Ono", "Ops Nakajima", "Pax Ueda", "Quies Matsuo", "Robigo Kikuchi", "Sol Sugiyama", "Tellus Takeda", "Unxia Arai", "Vesta Hirano",
    "Wizra Noguchi", "Xerxes Sugimoto", "Yal Chiba", "Zostera Nomura", "Acantha Kudo", "Balsam Sano", "Calyx Sugawara", "Daphne Kubo", "Erica Matsuura", "Fennel Kinoshita", "Galax Iwasaki", "Hazel Noguchi",
    "Iris Koyama", "Juniper Onishi", "Kalen Takagi", "Lotus Baba", "Myrtle Fukuda", "Nyssa Matsumoto", "Olive Shima", "Pansy Tanabe", "Quince Matsumura", "Rose Sawada", "Sage Ota", "Tansy Horie", "Ursinia Seki",
    "Viola Imai", "Willow Uchida", "Xanthium Yokoyama", "Yarrow Shimada", "Zinnia Yamauchi", "Alder Nakano", "Birch Masuda", "Cedar Katayama", "Dogwood Okazaki", "Elm Hirai", "Fir Noda", "Ginkgo Koga",
    "Hemlock Otsuka", "Ironwood Kawano", "Juniper Tajima", "Katsura Kamata", "Larch Shibuya", "Maple Mizuno", "Nyssa Kishimoto", "Oak Numata", "Pine Tsuji", "Quaking Inaba", "Redwood Okumura",
    "Spruce Kawaguchi", "Tupelo Shiraishi", "Upas Miyake", "Varnish Kitamura", "Walnut Kurata", "Xylosma Shinohara", "Yew Asano", "Zelkova Tani", "Abalone Hata", "Beryl Irie", "Coral Toyoda", "Diamond Kanda",
    "Emerald Nagai", "Flint Oki", "Garnet Komatsu", "Hyacinth Matsushima", "Iolite Ikeuchi", "Jade Sugita", "Kunzite Ozawa", "Lapis Shinozaki", "Moonstone Yoshioka", "Nephrite Kuroda", "Onyx Kase",
    "Pearl Kawashima", "Quartz Tsuchiya", "Ruby Fukui", "Sapphire Nanbu", "Topaz Arima", "Uvarovite Ishida", "Variscite Kumagai", "Wulfenite Shima", "Xenotime Tokunaga", "Yttrium Kasai",
    "Zircon Yanagi", "Amber Omori", "Basalt Takei", "Citrine Yasuda", "Dolomite Murata", "Epidote Hagiwara", "Feldspar Bessho", "Gypsum Oishi", "Hematite Kawahara", "Idocrase Sudo",
    "Jasper Hirayama", "Kyanite Ogura", "Lepidolite Nagasawa", "Malachite Kodama", "Natrolite Hirasawa", "Obsidian Kawada", "Peridot Katsura", "Rhodonite Enomoto", "Sodalite Tottori", "Turquoise Shiina",
    "Unakite Nakatani", "Vivianite Terada", "Wavellite Sugawara", "Xonotlite Shibazaki", "Yugawaralite Akimoto", "Zoisite Mitsui", "Altair Tsuru", "Bellatrix Shino", "Canopus Kitano", "Deneb Niwa",
    "Electra Shiro", "Fomalhaut Hoshino", "Gacrux Koyama", "Hadar Kanemoto", "Izar Higo", "Jabbah Arima", "Kaus Mogi", "Lesath Koshino", "Maia Shiota", "Nunki Inoue", "Okul Tsuda", "Pollux Serizawa", "Quat Okuma",
    "Rigel Shirai", "Sirius Kanda", "Talitha Horikoshi", "Unukalhai Sawa", "Vega Ohara", "Wasat Ebara", "Xylia Maki", "Yed Sugino", "Zaurak Shima", "Acamar Taira", "Beid Eguchi", "Castor Higa", "Diphda Shima", "Edasich Gushiken", "Furud Shima", "Gienah Uehara", "Homam Tamaki", "Imai Kina", "Jih Miyashiro",
    "Kraz Yonamine", "Lilii Shimabukuro", "Mebsuta Teruya", "Nihal Arakaki", "Okda Oshiro", "Phact Shima", "Rana Shima", "Sargas Shima", "Tejat Shima", "Usak Shima", "Vindemiatrix Shima", "Wazn Shima",
    "Xylos Shima", "Yildun Shima", "Zibal Shima", "Anka Smith", "Botein Johnson", "Chara Williams", "Denebola Brown", "Enif Jones", "Foramen Garcia", "Gomeisa Miller", "Hamal Davis", "Iklil Rodriguez",
    "Jabbah Martinez", "Keid Hernandez", "Larawag Lopez", "Miaplacidus Gonzalez", "Nashira Wilson", "Peacock Anderson", "Rasalgethi Thomas", "Skat Taylor", "Taygeta Moore", "Ukdah Jackson", "Veritate Martin",
    "Wurren Lee", "Xamidimura Perez", "Yvaine Thompson", "Zozma White", "Achernar Harris", "Baten Sanchez", "Canopus Clark", "Dabih Ramirez", "Eltanin Lewis", "Fumalsamakah Robinson", "Giedi Walker",
    "Hyadum Young", "Imai Allen", "Jih King", "Kaus Wright", "Lesath Scott", "Mebsuta Torres"
]

dataset = {
    "Python Programming": python_names,
    "Introduction to Machine Learning": ml_names,
}

# ==========================================
# 3. GENERATION ENGINE
# ==========================================
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_edx_dataset():
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
            serial_id = f"E{global_counter:03d}"
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
    generate_edx_dataset()
