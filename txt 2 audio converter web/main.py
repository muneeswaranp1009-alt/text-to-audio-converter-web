from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_tts():
    data = request.get_json()
    text = data.get('text')
    speed = data.get('speed', 'normal')

    if not text:
        return jsonify({'error': 'Please enter some text'}), 400

    try:
        if not os.path.exists(STATIC_DIR):
            os.makedirs(STATIC_DIR, exist_ok=True)

        filepath = os.path.join(STATIC_DIR, 'voice.mp3')
        
        is_slow = True if speed == 'slow' else False
        
        tts = gTTS(text=text, lang='en', slow=is_slow)
        tts.save(filepath)

        return jsonify({'audio_url': '/static/voice.mp3'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)