# MindCare AI - Mental Health FAQ Chatbot 🧠💬

A full-stack, AI-powered FAQ chatbot designed to answer common questions regarding mental health. This project was developed as part of the Artificial Intelligence Internship at CodeAlpha.

## Project Overview
MindCare AI utilizes Natural Language Processing (NLP) to understand user queries and match them with the most appropriate responses from a pre-processed dataset. The backend is powered by Python and Flask, utilizing `scikit-learn` and `NLTK` for the machine learning pipeline, while the frontend features a modern, responsive, glassmorphism UI built with HTML, CSS, and JavaScript.

## Features
* **Custom NLP Pipeline:** Implements tokenization, stop-word removal, and lemmatization using the Natural Language Toolkit (NLTK).
* **Mathematical Word Vectorization:** Uses `TfidfVectorizer` to convert text into meaningful numerical features.
* **Intent Matching:** Calculates `cosine_similarity` to accurately match user queries against the expanded FAQ dataset.
* **Fallback Logic:** Includes a confidence threshold to gracefully handle off-topic or unrecognized questions.
* **REST API Backend:** A lightweight Flask server that seamlessly handles asynchronous fetch requests from the frontend.
* **Modern UI/UX:** Features a glassmorphism aesthetic, animated gradient backgrounds, and dynamic "AI is thinking..." typing indicators.

## Tech Stack
* **Machine Learning & NLP:** Python, scikit-learn, NLTK, Pandas
* **Backend:** Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Development Environment:** Jupyter Notebook / Google Colab (for model training), local web server for deployment.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Muneebshah1192/CodeAlpha_FAQ_Chatbot.git](https://github.com/Muneebshah1192/CodeAlpha_FAQ_Chatbot.git)
   cd CodeAlpha_FAQ_Chatbot