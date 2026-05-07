import sqlite3
from config import DB_PATH


def get_certificate_details(serial_no):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM certificate WHERE serial_no=?",
        (serial_no,)
    )

    result = cursor.fetchone()

    conn.close()

    return result
