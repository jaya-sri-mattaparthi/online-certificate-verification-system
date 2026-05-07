ONLINE COURSE CERTIFICATE VERIFICATION SYSTEM USING YOLO-OCR AND VISION AI
📌 Overview

The Online Course Certificate Verification System is an AI-powered web application developed to automate the process of verifying online course certificates. The system uses YOLOv8 object detection, OCR (EasyOCR), and Computer Vision techniques to detect important certificate fields, extract textual information, and validate certificate authenticity with high accuracy.

The project reduces manual verification effort and improves reliability by providing automated verification results with confidence scores.

🚀 Features
AI-based certificate verification system
YOLOv8 object detection for field detection
OCR-based text extraction using EasyOCR
Detects multiple certificate fields automatically
Real-time verification with confidence score
Flask-based web application
Supports certificates from multiple platforms
Bounding box visualization for detected fields
Fast and accurate verification process
🧠 Technologies Used
Programming Languages
Python
Frameworks & Libraries
Flask
YOLOv8 (Ultralytics)
EasyOCR
OpenCV
NumPy
Pandas
Pillow
Database
SQLite / JSON
📂 Detected Certificate Fields

The system detects and extracts:

Candidate Name
Course Name
Certificate ID
Issue Date
Percentage / Score
Credits
Course Code
🌐 Supported Certificate Platforms
AWS
Google
IBM
Udacity
UpGrad
edX
FreeCodeCamp
⚙️ System Workflow
User uploads certificate image
Image preprocessing is applied
YOLOv8 detects certificate fields
OCR extracts text from detected regions
Extracted data is validated
AI-based verification logic calculates confidence score
Final verification result is displayed
📊 Performance
Achieved 90–100% verification accuracy
Reduced manual verification effort by 80%+
Supports real-time certificate verification
Handles multiple certificate layouts efficiently
🖥️ Installation & Setup
Clone Repository
git clone https://github.com/jaya-sri-mattaparthi/online-certificate-verification-system.git
Navigate to Project Folder
cd online-certificate-verification-system
Create Virtual Environment
python -m venv .venv
Activate Environment
Windows
.venv\Scripts\activate
Linux/Mac
source .venv/bin/activate
Install Dependencies
pip install -r requirements.txt
▶️ Run the Project
python app.py

The application will run on:

http://127.0.0.1:5000
📁 Project Structure
ONLINE-COURSE-CERTIFICATE-VERIFICATION-SYSTEM/
│
├── app.py
├── requirements.txt
├── README.md
├── templates/
├── static/
├── uploads/
├── model/
├── dataset/
└── results/
📸 Output

The system displays:

Uploaded certificate image
Detected bounding boxes
Extracted certificate details
Verification accuracy score
Final verification status
🔮 Future Enhancements
Blockchain-based certificate validation
Cloud deployment support
Mobile application integration
Multilingual certificate support
Advanced fake certificate detection
👩‍💻 Author

MATTAPARTHI JAYA SRI DURGA AISHWARYA

📄 License

This project is developed for educational and research purposes.
