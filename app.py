from flask import Flask, render_template, request, jsonify
import requests
import base64
import logging

app = Flask(__name__)

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG)

# Ganti dengan Access Token Anda
HUGGINGFACE_ACCESS_TOKEN = "YOUR-TOKEN"

# URL endpoint untuk setiap model
ASR_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"
LLM_API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
TTS_API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-ind"

headers = {"Authorization": f"Bearer {HUGGINGFACE_ACCESS_TOKEN}"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        audio_file = request.files['audio']
        
        # Speech to Text
        logging.debug("Sending request to ASR API")
        asr_response = requests.post(ASR_API_URL, headers=headers, data=audio_file)
        asr_response.raise_for_status()
        text = asr_response.json().get('text', '')
        logging.debug(f"ASR Result: {text}")
        
        # LLM Processing
        logging.debug("Sending request to LLM API")
        llm_response = requests.post(LLM_API_URL, headers=headers, json={"inputs": text})
        llm_response.raise_for_status()
        llm_text = llm_response.json()[0].get('generated_text', '')
        logging.debug(f"LLM Response: {llm_text}")
        
        # Text to Speech (hanya untuk jawaban LLM)
        logging.debug("Sending request to TTS API")
        tts_response = requests.post(TTS_API_URL, headers=headers, json={"inputs": llm_text})
        tts_response.raise_for_status()
        
        # Check content type
        content_type = tts_response.headers.get('content-type', '')
        logging.debug(f"TTS Response Content-Type: {content_type}")
        
        if 'audio' in content_type:
            audio_content = tts_response.content
            audio_base64 = base64.b64encode(audio_content).decode('utf-8')
            logging.debug("Audio content successfully encoded")
        else:
            logging.error("Received non-audio response from TTS API")
            return jsonify({'error': 'Received non-audio response from TTS API'})
        
        return jsonify({
            'question': text,  # Pertanyaan asli dari speech-to-text
            'answer': llm_text,  # Jawaban dari LLM
            'audio': audio_base64  # Audio dari jawaban LLM
        })
    
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {str(e)}")
        return jsonify({'error': f"API request failed: {str(e)}"}), 500
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
