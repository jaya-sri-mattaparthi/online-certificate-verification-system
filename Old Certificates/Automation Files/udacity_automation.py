import os
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# 1. CONFIGURATION (AWS Template Calibration)
# ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "udacity.png")
OUTPUT_DIR = "Udacity_Certificates"

# UNIFIED FONT STYLE
FONT_STYLE = r"C:\Windows\Fonts\arialbd.ttf"

# TEXT SIZES
NAME_SIZE = 30
COURSE_SIZE = 30
SERIAL_SIZE = 30

# COORDINATES
NAME_X, NAME_Y = 670, 590
COURSE_X, COURSE_Y = 580, 430
SERIAL_X, SERIAL_Y = 1150, 880

# COLORS (Matched to AWS Charcoal Grey)
TEXT_COLOR = (35, 31, 32)

# ==========================================
# 2. 150 UNIQUE NAMES (Divided by AWS Course)
# ==========================================
algo_names = [
    "Liam Smith", "Liam Johnson", "Liam Williams", "Liam Brown", "Liam Jones", "Liam Garcia",
    "Liam Miller", "Liam Davis", "Liam Rodriguez", "Liam Martinez", "Noah Smith", "Noah Johnson", "Noah Williams", "Noah Brown", "Noah Jones", "Noah Garcia", "Noah Miller", "Noah Davis", "Noah Rodriguez",
    "Noah Martinez", "Oliver Smith", "Oliver Johnson", "Oliver Williams", "Oliver Brown", "Oliver Jones", "Oliver Garcia", "Oliver Miller", "Oliver Davis", "Oliver Rodriguez", "Oliver Martinez", "Elijah Smith",
    "Elijah Johnson", "Elijah Williams", "Elijah Brown", "Elijah Jones", "Elijah Garcia", "Elijah Miller", "Elijah Davis", "Elijah Rodriguez", "Elijah Martinez", "William Smith", "William Johnson",
    "William Williams", "William Brown", "William Jones", "William Garcia", "William Miller", "William Davis", "William Rodriguez", "William Martinez", "James Smith", "James Johnson", "James Williams", "James Brown",
    "James Jones", "James Garcia", "James Miller", "James Davis", "James Rodriguez", "James Martinez", "Benjamin Smith", "Benjamin Johnson", "Benjamin Williams", "Benjamin Brown", "Benjamin Jones",
    "Benjamin Garcia", "Benjamin Miller", "Benjamin Davis", "Benjamin Rodriguez", "Benjamin Martinez", "Lucas Smith", "Lucas Johnson", "Lucas Williams", "Lucas Brown", "Lucas Jones", "Lucas Garcia", "Lucas Miller",
    "Lucas Davis", "Lucas Rodriguez", "Lucas Martinez", "Henry Smith", "Henry Johnson", "Henry Williams", "Henry Brown", "Henry Jones", "Henry Garcia", "Henry Miller", "Henry Davis", "Henry Rodriguez",
    "Henry Martinez", "Alexander Smith", "Alexander Johnson", "Alexander Williams", "Alexander Brown", "Alexander Jones", "Alexander Garcia", "Alexander Miller", "Alexander Davis", "Alexander Rodriguez",
    "Alexander Martinez", "Mason Smith", "Mason Johnson", "Mason Williams", "Mason Brown", "Mason Jones", "Mason Garcia", "Mason Miller", "Mason Davis", "Mason Rodriguez", "Mason Martinez", "Michael Smith",
    "Michael Johnson", "Michael Williams", "Michael Brown", "Michael Jones", "Michael Garcia", "Michael Miller", "Michael Davis", "Michael Rodriguez", "Michael Martinez", "Ethan Smith", "Ethan Johnson",
    "Ethan Williams", "Ethan Brown", "Ethan Jones", "Ethan Garcia", "Ethan Miller", "Ethan Davis", "Ethan Rodriguez", "Ethan Martinez", "Daniel Smith", "Daniel Johnson", "Daniel Williams", "Daniel Brown",
    "Daniel Jones", "Daniel Garcia", "Daniel Miller", "Daniel Davis", "Daniel Rodriguez", "Daniel Martinez", "Jacob Smith", "Jacob Johnson", "Jacob Williams", "Jacob Brown", "Jacob Jones", "Jacob Garcia", "Jacob Miller",
    "Jacob Davis", "Jacob Rodriguez", "Jacob Martinez", "Logan Smith", "Logan Johnson", "Logan Williams", "Logan Brown", "Logan Jones", "Logan Garcia", "Logan Miller", "Logan Davis", "Logan Rodriguez", "Logan Martinez",
    "Jackson Smith", "Jackson Johnson", "Jackson Williams", "Jackson Brown", "Jackson Jones", "Jackson Garcia", "Jackson Miller", "Jackson Davis", "Jackson Rodriguez", "Jackson Martinez", "Levi Smith", "Levi Johnson",
    "Levi Williams", "Levi Brown", "Levi Jones", "Levi Garcia", "Levi Miller", "Levi Davis", "Levi Rodriguez", "Levi Martinez", "Sebastian Smith", "Sebastian Johnson", "Sebastian Williams", "Sebastian Brown", "Sebastian Jones",
    "Sebastian Garcia", "Sebastian Miller", "Sebastian Davis", "Sebastian Rodriguez", "Sebastian Martinez", "Mateo Smith", "Mateo Johnson", "Mateo Williams", "Mateo Brown", "Mateo Jones", "Mateo Garcia", "Mateo Miller",
    "Mateo Davis", "Mateo Rodriguez", "Mateo Martinez", "Jack Smith", "Jack Johnson", "Jack Williams", "Jack Brown", "Jack Jones", "Jack Garcia", "Jack Miller", "Jack Davis", "Jack Rodriguez", "Jack Martinez", "Owen Smith",
    "Owen Johnson", "Owen Williams", "Owen Brown", "Owen Jones", "Owen Garcia", "Owen Miller", "Owen Davis", "Owen Rodriguez", "Owen Martinez", "Theodore Smith", "Theodore Johnson", "Theodore Williams", "Theodore Brown",
    "Theodore Jones", "Theodore Garcia", "Theodore Miller", "Theodore Davis", "Theodore Rodriguez", "Theodore Martinez", "Aiden Smith", "Aiden Johnson", "Aiden Williams", "Aiden Brown", "Aiden Jones", "Aiden Garcia",
    "Aiden Miller", "Aiden Davis", "Aiden Rodriguez", "Aiden Martinez", "Samuel Smith", "Samuel Johnson", "Samuel Williams", "Samuel Brown", "Samuel Jones", "Samuel Garcia", "Samuel Miller", "Samuel Davis", "Samuel Rodriguez",
    "Samuel Martinez", "Joseph Smith", "Joseph Johnson", "Joseph Williams", "Joseph Brown", "Joseph Jones", "Joseph Garcia", "Joseph Miller", "Joseph Davis", "Joseph Rodriguez", "Joseph Martinez", "John Smith", "John Johnson",
    "John Williams", "John Brown", "John Jones", "John Garcia", "John Miller", "John Davis", "John Rodriguez", "John Martinez", "David Smith", "David Johnson", "David Williams", "David Brown", "David Jones", "David Garcia",
    "David Miller", "David Davis", "David Rodriguez", "David Martinez", "Wyatt Smith", "Wyatt Johnson", "Wyatt Williams", "Wyatt Brown", "Wyatt Jones", "Wyatt Garcia", "Wyatt Miller", "Wyatt Davis", "Wyatt Rodriguez",
    "Wyatt Martinez", "Matthew Smith", "Matthew Johnson", "Matthew Williams", "Matthew Brown", "Matthew Jones", "Matthew Garcia", "Matthew Miller", "Matthew Davis", "Matthew Rodriguez", "Matthew Martinez"
]

dl_names = [
    "Luke Smith",
    "Luke Johnson", "Luke Williams", "Luke Brown", "Luke Jones", "Luke Garcia", "Luke Miller", "Luke Davis", "Luke Rodriguez", "Luke Martinez", "Asher Smith", "Asher Johnson", "Asher Williams", "Asher Brown", "Asher Jones",
    "Asher Garcia", "Asher Miller", "Asher Davis", "Asher Rodriguez", "Asher Martinez", "Carter Smith", "Carter Johnson", "Carter Williams", "Carter Brown", "Carter Jones", "Carter Garcia", "Carter Miller", "Carter Davis",
    "Carter Rodriguez", "Carter Martinez", "Julian Smith", "Julian Johnson", "Julian Williams", "Julian Brown", "Julian Jones", "Julian Garcia", "Julian Miller", "Julian Davis", "Julian Rodriguez", "Julian Martinez",
    "Grayson Smith", "Grayson Johnson", "Grayson Williams", "Grayson Brown", "Grayson Jones", "Grayson Garcia", "Grayson Miller", "Grayson Davis", "Grayson Rodriguez", "Grayson Martinez", "Leo Smith", "Leo Johnson",
    "Leo Williams", "Leo Brown", "Leo Jones", "Leo Garcia", "Leo Miller", "Leo Davis", "Leo Rodriguez", "Leo Martinez", "Jayden Smith", "Jayden Johnson", "Jayden Williams", "Jayden Brown", "Jayden Jones", "Jayden Garcia",
    "Jayden Miller", "Jayden Davis", "Jayden Rodriguez", "Jayden Martinez", "Gabriel Smith", "Gabriel Johnson", "Gabriel Williams", "Gabriel Brown", "Gabriel Jones", "Gabriel Garcia", "Gabriel Miller", "Gabriel Davis",
    "Gabriel Rodriguez", "Gabriel Martinez", "Isaac Smith", "Isaac Johnson", "Isaac Williams", "Isaac Brown", "Isaac Jones", "Isaac Garcia", "Isaac Miller", "Isaac Davis", "Isaac Rodriguez", "Isaac Martinez", "Lincoln Smith",
    "Lincoln Johnson", "Lincoln Williams", "Lincoln Brown", "Lincoln Jones", "Lincoln Garcia", "Lincoln Miller", "Lincoln Davis", "Lincoln Rodriguez", "Lincoln Martinez", "Anthony Smith", "Anthony Johnson",
    "Anthony Williams", "Anthony Brown", "Anthony Jones", "Anthony Garcia", "Anthony Miller", "Anthony Davis", "Anthony Rodriguez", "Anthony Martinez", "Hudson Smith", "Hudson Johnson", "Hudson Williams", "Hudson Brown",
    "Hudson Jones", "Hudson Garcia", "Hudson Miller", "Hudson Davis", "Hudson Rodriguez", "Hudson Martinez", "Dylan Smith", "Dylan Johnson", "Dylan Williams", "Dylan Brown", "Dylan Jones", "Dylan Garcia", "Dylan Miller",
    "Dylan Davis", "Dylan Rodriguez", "Dylan Martinez", "Ezra Smith", "Ezra Johnson", "Ezra Williams", "Ezra Brown", "Ezra Jones", "Ezra Garcia", "Ezra Miller", "Ezra Davis", "Ezra Rodriguez", "Ezra Martinez", "Thomas Smith",
    "Thomas Johnson", "Thomas Williams", "Thomas Brown", "Thomas Jones", "Thomas Garcia", "Thomas Miller", "Thomas Davis", "Thomas Rodriguez", "Thomas Martinez", "Charles Smith", "Charles Johnson", "Charles Williams",
    "Charles Brown", "Charles Jones", "Charles Garcia", "Charles Miller", "Charles Davis", "Charles Rodriguez", "Charles Martinez", "Christopher Smith", "Christopher Johnson", "Christopher Williams", "Christopher Brown",
    "Christopher Jones", "Christopher Garcia", "Christopher Miller", "Christopher Davis", "Christopher Rodriguez", "Christopher Martinez", "Jaxon Smith", "Jaxon Johnson", "Jaxon Williams", "Jaxon Brown", "Jaxon Jones",
    "Jaxon Garcia", "Jaxon Miller", "Jaxon Davis", "Jaxon Rodriguez", "Jaxon Martinez", "Maverick Smith", "Maverick Johnson", "Maverick Williams", "Maverick Brown", "Maverick Jones", "Maverick Garcia",
    "Maverick Miller", "Maverick Davis", "Maverick Rodriguez", "Maverick Martinez", "Josiah Smith", "Josiah Johnson", "Josiah Williams", "Josiah Brown", "Josiah Jones", "Josiah Garcia", "Josiah Miller",
    "Josiah Davis", "Josiah Rodriguez", "Josiah Martinez", "Isaiah Smith", "Isaiah Johnson", "Isaiah Williams", "Isaiah Brown", "Isaiah Jones", "Isaiah Garcia", "Isaiah Miller",
    "Isaiah Davis", "Isaiah Rodriguez", "Isaiah Martinez", "Andrew Smith", "Andrew Johnson", "Andrew Williams", "Andrew Brown", "Andrew Jones", "Andrew Garcia", "Andrew Miller", "Andrew Davis", "Andrew Rodriguez",
    "Andrew Martinez", "Elias Smith", "Elias Johnson", "Elias Williams", "Elias Brown", "Elias Jones", "Elias Garcia", "Elias Miller", "Elias Davis", "Elias Rodriguez", "Elias Martinez", "Joshua Smith",
    "Joshua Johnson", "Joshua Williams", "Joshua Brown", "Joshua Jones", "Joshua Garcia", "Joshua Miller", "Joshua Davis", "Joshua Rodriguez", "Joshua Martinez", "Nathan Smith", "Nathan Johnson", "Nathan Williams",
    "Nathan Brown", "Nathan Jones", "Nathan Garcia", "Nathan Miller", "Nathan Davis", "Nathan Rodriguez", "Nathan Martinez", "Caleb Smith", "Caleb Johnson", "Caleb Williams", "Caleb Brown", "Caleb Jones",
    "Caleb Garcia", "Caleb Miller", "Caleb Davis", "Caleb Rodriguez", "Caleb Martinez", "Ryan Smith", "Ryan Johnson", "Ryan Williams", "Ryan Brown", "Ryan Jones", "Ryan Garcia", "Ryan Miller", "Ryan Davis",
    "Ryan Rodriguez", "Ryan Martinez", "Adrian Smith", "Adrian Johnson", "Adrian Williams", "Adrian Brown", "Adrian Jones", "Adrian Garcia", "Adrian Miller", "Adrian Davis", "Adrian Rodriguez", "Adrian Martinez", "Miles Smith",
    "Miles Johnson", "Miles Williams", "Miles Brown", "Miles Jones", "Miles Garcia", "Miles Miller", "Miles Davis", "Miles Rodriguez", "Miles Martinez", "Eli Smith", "Eli Johnson", "Eli Williams", "Eli Brown", "Eli Jones",
    "Eli Garcia", "Eli Miller", "Eli Davis", "Eli Rodriguez", "Eli Martinez"
]

dataset = {
    "Introduction to Algorithms": algo_names,
    "Introduction to Deep Learning": dl_names,
}

# ==========================================
# 3. GENERATION ENGINE
# ==========================================
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_udacity_dataset():
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
            serial_id = f"D{global_counter:03d}"
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
    generate_udacity_dataset()
