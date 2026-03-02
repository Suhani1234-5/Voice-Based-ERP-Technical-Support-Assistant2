from groq import Groq
from config import GROQ_API_KEY, GROQ_STT_MODEL
import tempfile
import os

client = None
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)

def transcribe_audio(audio_bytes):
    if not client:
        return "Error: GROQ_API_KEY is not set. Please add it to Streamlit Secrets."
    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        with open(tmp_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=GROQ_STT_MODEL,  # Groq ka fast whisper
                file=("audio.wav", audio_file),
                response_format="text"
            )

        os.unlink(tmp_path)
        return transcription

    except Exception as e:
        return f"Error in transcription: {str(e)}"