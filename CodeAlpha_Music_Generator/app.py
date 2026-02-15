import os
import time
import pickle
import numpy as np
import random
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from keras.models import load_model
from music21 import instrument, note, stream, chord

app = Flask(__name__)
CORS(app)

# Ensure static directory exists
os.makedirs('static', exist_ok=True)

# Load Model and Mapping
model = load_model('models/music_generator_model.h5')
with open('models/pitchnames.pkl', 'rb') as f:
    pitchnames = pickle.load(f)

n_vocab = len(pitchnames)
int_to_note = {i: n for i, n in enumerate(pitchnames)}

def sample_with_temperature(preds, temperature=0.8):
    """Adds variety by sampling from the probability distribution."""
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-7) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

@app.route('/generate', methods=['GET'])
def generate():
    try:
        # Generate 150 notes for a longer, more complex song
        sequence_length = 100
        pattern = [random.randint(0, n_vocab - 1) for _ in range(sequence_length)]
        prediction_output = []

        for _ in range(150):
            prediction_input = np.reshape(pattern, (1, len(pattern), 1))
            prediction_input = prediction_input / float(n_vocab)
            
            prediction = model.predict(prediction_input, verbose=0)[0]
            # Use temperature sampling for variety
            index = sample_with_temperature(prediction, temperature=0.8)
            
            prediction_output.append(int_to_note[index])
            pattern.append(index)
            pattern = pattern[1:]

        # Convert AI notes back to MIDI
        offset = 0
        output_notes = []
        for p_note in prediction_output:
            if ('.' in p_note) or p_note.isdigit():
                notes_in_chord = p_note.split('.')
                notes = [note.Note(int(n)) for n in notes_in_chord]
                for n in notes: n.storedInstrument = instrument.Piano()
                new_chord = chord.Chord(notes)
                new_chord.offset = offset
                output_notes.append(new_chord)
            else:
                new_note = note.Note(p_note)
                new_note.offset = offset
                new_note.storedInstrument = instrument.Piano()
                output_notes.append(new_note)
            offset += 0.5

        midi_stream = stream.Stream(output_notes)
        filename = f"track_{int(time.time())}.mid"
        filepath = os.path.join('static', filename)
        midi_stream.write('midi', fp=filepath)
        
        # Verify file was created
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"✅ MIDI file created: {filename} ({file_size} bytes)")
        else:
            print(f"❌ Failed to create MIDI file: {filename}")

        return jsonify({
            "status": "success", 
            "file_url": f"http://127.0.0.1:5000/static/{filename}"
        })
    except Exception as e:
        print(f"❌ Error in generate: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/static/<path:filename>')
def serve_static(filename):
    try:
        return send_from_directory('static', filename)
    except Exception as e:
        print(f"❌ Error serving {filename}: {str(e)}")
        return jsonify({"error": "File not found"}), 404

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "static_dir_exists": os.path.exists('static')})

if __name__ == '__main__':
    print("🎵 Neural Symphony Studio Backend")
    print(f"📁 Static directory: {os.path.abspath('static')}")
    print("🚀 Server starting on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)