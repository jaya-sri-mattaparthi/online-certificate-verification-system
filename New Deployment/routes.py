import os
from flask import render_template, request
from werkzeug.utils import secure_filename

from ocr import extract_fields
from agent import ai_agent_extract
from db import get_certificate_details
from verifier import overall_verification_accuracy


def register_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def index():

        if request.method == "POST":

            serial_no = request.form["serial"]
            platform = request.form.get("platform", "")
            model_type = request.form.get("model", "ocr")  # OCR or AI Agent
            image = request.files["image"]

            # save uploaded file
            filename = secure_filename(image.filename)
            upload_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image.save(upload_path)

            annotated_filename = None
            extracted_fields = {}

            # =========================
            # Choose model
            # =========================

            if model_type == "ai":

                # AI Agent extraction
                extracted_fields = ai_agent_extract(upload_path)

            else:

                # OCR extraction with annotation
                annotated_filename = f"annotated_{filename}"
                annotated_path = os.path.join(
                    app.config["UPLOAD_FOLDER"], annotated_filename
                )

                extracted_fields = extract_fields(upload_path, annotated_path)

            # =========================
            # Database verification
            # =========================

            db_result = get_certificate_details(serial_no)

            overall_accuracy = overall_verification_accuracy(
                extracted_fields, db_result
            )

            # =========================
            # Verification status
            # =========================

            if overall_accuracy > 90:
                status = "Verified Successfully"
            else:
                status = "Verification Failed"

            return render_template(
                "result.html",
                accuracy=overall_accuracy,
                status=status,
                uploaded=filename,
                annotated=annotated_filename,
                platform=platform
            )

        return render_template("index.html")
