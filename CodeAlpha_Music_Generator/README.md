# AI Music Generation Studio 🎵🤖

An autonomous music composition engine developed during the CodeAlpha Artificial Intelligence Internship. This project leverages Deep Learning and Recurrent Neural Networks (RNNs) to understand the mathematical sequences of music and generate original piano and orchestral motifs.

## ✨ Features
* **AI-Powered Composition:** Generates unique, non-repetitive musical sequences using advanced neural network architecture.
* **MIDI Processing:** Utilizes the `music21` library to parse complex MIDI files, extracting pitch, duration, and rhythm as mathematically processable vectors.
* **Long Short-Term Memory (LSTM):** Employs memory gates to retain long-term dependencies, ensuring melodies maintain a consistent key and rhythmic structure.
* **Temperature Sampling:** Integrates calculated randomness to prevent the "repetitive tune" problem, allowing the AI to take creative risks.
* **Full-Stack Deployment:** Features a Python/Flask API backend connected to a sleek "Midnight Silk" glassmorphism web interface.
* **In-Browser Synthesis:** Preview AI-generated tracks directly in the browser using digital instruments.

## 🛠️ Technology Stack
* **AI/Machine Learning:** Python, Keras/TensorFlow, `music21`
* **Backend:** Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, JavaScript (MidiPlayer.js, Soundfont-player)
* **Architecture:** LSTM Neural Networks with Dropout Regularization

## 📂 Project Structure
```text
CodeAlpha_Music_Generator/
├── app.py                 # The Python Flask backend API
├── models/                # Trained LSTM neural network models (.h5)
├── README.md              # Project documentation
└── templates/             
    └── index.html         # The Glassmorphism UI (Frontend)
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muneebshah1192/CodeAlpha_Tasks.git
   cd CodeAlpha_Tasks/CodeAlpha_Music_Generator
   ```
2. **Install the required Python dependencies:**
   ```bash
   pip install flask flask-cors music21 tensorflow keras numpy
   ```
3. **Run the Backend Server:**
   ```bash
   python app.py
   ```
4. **Launch the Application:**
   Open your web browser and navigate to:
   `http://127.0.0.1:5000`

## 👨‍💻 Author
**Syed Muneeb Haider Shah** *Information Technology Student at The University Of Chakwal* *Artificial Intelligence Intern at CodeAlpha*

---
*Developed February 2026*
