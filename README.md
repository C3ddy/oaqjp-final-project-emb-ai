# Emotion Detection Web Application

## 📌 Overview
This project is an AI-powered web application that analyzes text input and detects emotions such as anger, disgust, fear, joy, and sadness, along with identifying the dominant emotion.

It was developed as part of the IBM Python for AI & Development final project.

---

## 🚀 Features
- Analyze user input text for emotional tone
- Detect multiple emotions:
  - Anger
  - Disgust
  - Fear
  - Joy
  - Sadness
- Identify the dominant emotion
- Web interface built with Flask
- Unit tested with Python unittest
- Code quality enforced with pylint

---

## 🧠 How It Works
The application sends user input to an emotion detection module powered by NLP.

Steps:
1. Receives text input
2. Processes it using an emotion detection API
3. Returns emotion scores
4. Determines the dominant emotion

---

## 🛠️ Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Testing: unittest
- Linting: pylint
- AI/NLP: Watson NLP API

---

## 📂 Project Structure
.
├── EmotionDetection/
├── static/
├── templates/
├── server.py
├── test_emotion_detection.py
├── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/C3ddy/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the application
python server.py

### 4. Open in browser
http://localhost:5000

---

## 🧪 Running Tests
python -m unittest test_emotion_detection.py

---

## ⚠️ Important Note
This project may require access to IBM Watson NLP services. Without proper credentials, API calls may fail.

---

## 🎯 Learning Objectives
- Build a Flask-based web application
- Integrate external AI APIs
- Write unit tests
- Apply linting tools
- Structure a full-stack project

---

## 📸 Example

Input:
I am really happy today!

Output:
joy: 0.95  
dominant emotion: joy

---

## 📄 License
Apache 2.0 License

---

## 👤 Author
Cedrick Picard

---

## 💡 Improvements (Future Work)
- Add real-time analysis (AJAX)
- Improve UI/UX
- Add authentication
- Deploy to cloud
