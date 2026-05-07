import sqlite3

conn = sqlite3.connect("certificate.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS certificate (
    serial_no TEXT PRIMARY KEY,
    student_name TEXT,
    course_name TEXT,
    issued_on TEXT,
    course_code TEXT,
    percentage TEXT,
    credits TEXT
)
""")

conn.commit()
conn.close()

print("Database created!")
