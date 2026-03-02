from gtts import gTTS
import tempfile
import os

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as tmp:
            tmp_path = tmp.name
        
        tts.save(tmp_path)
        
        with open(tmp_path, "rb") as f:
            audio_bytes = f.read()
        
        os.unlink(tmp_path)
        return audio_bytes
        
    except Exception as e:
        print(f"TTS Error: {str(e)}")
        return None