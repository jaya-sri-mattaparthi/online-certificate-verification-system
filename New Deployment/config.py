import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
MODEL_PATH = os.path.join(BASE_DIR, "best.pt")

DB_PATH = r"C:\Users\saisa\Desktop\New Project\New Deployment\certificate.db"

FIELD_NAMES = {
    0: "Course Code",
    1: "Course Name",
    2: "Credits",
    3: "Issued On",
    4: "Percentage",
    5: "Serial No",
    6: "Student Name"
}
