from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)
CORS(app) 

# Download necessary NLTK data for local processing
nltk.download('punkt')
nltk.download('punkt_tab')  
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

# Load the models trained in Colab
print("Loading models...")
try:
    with open('models/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('models/tfidf_matrix.pkl', 'rb') as f:
        tfidf_matrix = pickle.load(f)
    df = pd.read_pickle('models/dataset.pkl')
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    print("Make sure vectorizer.pkl, tfidf_matrix.pkl, and dataset.pkl are inside the 'models' folder.")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # 1. Lowercase
    text = str(text).lower()
    # 2. Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # 3. Tokenize
    tokens = word_tokenize(text)
    # 4. Remove stopwords and lemmatize
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(cleaned_tokens)

@app.route('/ask', methods=['POST'])
def ask_chatbot():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"answer": "Please ask a valid question."})

    # Process input and find the best match
    cleaned_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([cleaned_input])
    similarity_scores = cosine_similarity(input_vector, tfidf_matrix)
    
    best_match_index = similarity_scores.argmax()
    highest_score = similarity_scores[0, best_match_index]
    
    # Fallback response if the confidence is too low
    if highest_score < 0.20:
        return jsonify({"answer": "I'm sorry, I don't have enough information on that specific topic. Could you rephrase your question?"})
    
    answer = df['Answer'].iloc[best_match_index]
    return jsonify({"answer": answer})

if __name__ == '__main__':
    print("Starting server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)