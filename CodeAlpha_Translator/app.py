from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)

print("--- Initializing AI Neural Translator ---")

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
      
        data = request.json
        text = data.get('text', '')
        target_lang = data.get('target', 'ur') 
        source_lang = data.get('source', 'auto')

        if not text:
            return jsonify({'status': 'error', 'message': 'No text provided'})

        print(f"Translating to {target_lang}: {text[:20]}...")

        # Perform Neural Machine Translation
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)

        return jsonify({
            'status': 'success', 
            'original': text,
            'translated': translated
        })

    except Exception as e:
        print(f"Translation Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)