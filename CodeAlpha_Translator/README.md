# Global AI Translator 🌍

A real-time, multilingual Natural Language Processing (NLP) web application built during the CodeAlpha Artificial Intelligence Internship. This tool leverages Neural Machine Translation (NMT) to provide accurate, context-aware text translations across multiple global languages.

## ✨ Features
* **Real-Time Translation:** Powered by the `deep-translator` engine for fast, API-driven results.
* **Auto-Language Detection:** Automatically identifies the source language.
* **Multilingual Support:** Translates between English, Urdu, French, Spanish, Arabic, Chinese, and Japanese.
* **Premium UI/UX:** Features a "Midnight Silk" glassmorphism aesthetic with a responsive, dual-pane design.
* **Smart Copy:** Built-in "Copy to Clipboard" functionality with visual feedback.
* **Asynchronous Processing:** Zero page-reloads utilizing the JavaScript Fetch API.

## 🛠️ Technology Stack
* **Backend:** Python 3.x, Flask, Flask-CORS
* **AI Engine:** `deep-translator` (Neural Machine Translation)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript

## 📂 Project Structure
```text
CodeAlpha_Translator/
├── app.py                 # The Python Flask backend API
├── README.md              # Project documentation
└── templates/             
    └── index.html         # The Glassmorphism UI (Frontend)
```

## 🚀 Installation & Setup

1. **Clone or Download** this repository to your local machine.
2. **Install the required Python dependencies:**
   Open your terminal and run:
   ```bash
   pip install flask flask-cors deep-translator
   ```
3. **Run the Backend Server:**
   ```bash
   python app.py
   ```
4. **Launch the Application:**
   Open your web browser and navigate to:
   `http://127.0.0.1:5000`

## 💡 Usage
1. Paste or type the text you want to translate into the left text box.
2. Select your desired Target Language from the dropdown menu on the right.
3. Click the **"Translate Now"** button.
4. Once processed, use the **"Copy"** button to instantly save your translated text to your clipboard.

## 👨‍💻 Author
**Syed Muneeb Haider Shah** *Information Technology Student at The University Of Chakwal* *Artificial Intelligence Intern at CodeAlpha*

---
*Developed February 2026*
