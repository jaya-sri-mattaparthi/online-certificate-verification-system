import sqlite3
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_PATH = os.path.join(BASE_DIR, "database.json")
DB_PATH = os.path.join(BASE_DIR, "certificate.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open(JSON_PATH) as f:
    data = json.load(f)

for image, details in data.items():

    cursor.execute("""
        INSERT OR REPLACE INTO certificate
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        details.get("Serial No"),
        details.get("Student Name"),
        details.get("Course Name"),
        details.get("Issued On"),
        details.get("Course Code"),
        details.get("Percentage"),
        details.get("Credits")
    ))

conn.commit()
conn.close()

print("Data inserted!")
