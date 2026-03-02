import requests
import os
import tempfile

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_STT_MODEL = "whisper-large-v3"

def transcribe_audio(audio_bytes):
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY not set in Streamlit Secrets."

    try:
        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        url = "https://api.groq.com/openai/v1/audio/transcriptions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }

        files = {
            "file": ("audio.wav", open(tmp_path, "rb"), "audio/wav")
        }

        data = {
            "model": GROQ_STT_MODEL
        }

        response = requests.post(url, headers=headers, files=files, data=data)

        os.unlink(tmp_path)

        if response.status_code == 200:
            return response.json()["text"]
        else:
            return f"Groq API Error: {response.text}"

    except Exception as e:
        return f"🎤 Error in transcription: {str(e)}"