from flask import Flask
import os

from config import UPLOAD_FOLDER
from routes import register_routes

# serve uploads as static files
app = Flask(__name__, static_url_path="/uploads", static_folder=UPLOAD_FOLDER)

# create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
