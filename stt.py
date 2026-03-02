from groq import Groq
import os
import tempfile

# Get API key from environment (Streamlit Secrets automatically loads this)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# You can hardcode if needed:
# GROQ_STT_MODEL = "whisper-large-v3"
GROQ_STT_MODEL = "whisper-large-v3"

# Initialize client only if key exists
client = None
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)


def transcribe_audio(audio_bytes):
    if not client:
        return "Error: GROQ_API_KEY is not set. Please add it in Streamlit Secrets."

    try:
        # Save audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        # Open and send to Groq
        with open(tmp_path, "rb") as audio_file:
            response = client.audio.transcriptions(
                file=("audio.wav", audio_file),
                model=GROQ_STT_MODEL,
            )

        # Delete temp file
        os.unlink(tmp_path)

        # Return transcribed text
        return response.text

    except Exception as e:
        return f"🎤 Error in transcription: {str(e)}"