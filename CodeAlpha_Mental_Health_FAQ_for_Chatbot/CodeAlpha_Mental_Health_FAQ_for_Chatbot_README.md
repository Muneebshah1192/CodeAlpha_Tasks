# MindCare AI: Mental Health FAQ Chatbot 🧠💬

An intelligent, NLP-powered FAQ chatbot developed during the CodeAlpha Artificial Intelligence Internship. This project is designed to provide immediate, context-aware answers to user inquiries regarding mental health by matching conversational input against a curated dataset.

## ✨ Features
* **Natural Language Processing (NLP):** Utilizes the NLTK library to normalize, tokenize, and lemmatize raw user text, removing noise and isolating core concepts.
* **Mathematical Semantic Matching:** Employs **TF-IDF Vectorization** and **Cosine Similarity** to mathematically calculate the closest matching question in the dataset, rather than relying on brittle keyword matching.
* **Data Augmentation:** The core Kaggle dataset was programmatically expanded with conversational prefixes to increase the model's resilience to varied user phrasing.
* **Responsive UI:** Features a modern, asynchronous "Glassmorphism" web interface that provides a seamless chat experience with real-time "AI is thinking..." animations.

## 🛠️ Technology Stack
* **Core Logic:** Python 3.x
* **Machine Learning / NLP:** `scikit-learn` (TfidfVectorizer, cosine_similarity), `nltk`, `pandas`
* **Backend:** Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)

## 📂 Project Structure
```text
CodeAlpha_Mental_Health_FAQ_for_Chatbot/
├── app.py                 # The Python Flask backend API
├── Mental_Health_FAQ_for_Chatbot_by_Muneeb_1000.csv # The expanded dataset
├── models/                # Serialized (.pkl) vectorizers and matrices
├── README.md              # Project documentation
└── templates/             
    └── index.html         # The Chatbot Web UI
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muneebshah1192/CodeAlpha_Tasks.git
   cd CodeAlpha_Tasks/CodeAlpha_Mental_Health_FAQ_for_Chatbot
   ```
2. **Install the required dependencies:**
   ```bash
   pip install flask flask-cors pandas scikit-learn nltk
   ```
3. **Run the Server:**
   ```bash
   python app.py
   ```
   *(Note: The server will automatically download the necessary NLTK corpora during initialization).*
4. **Chat with MindCare AI:**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 👨‍💻 Author
**Syed Muneeb Haider Shah** *Information Technology Student at The University Of Chakwal* *Artificial Intelligence Intern at CodeAlpha*

---
*Developed February 2026*
