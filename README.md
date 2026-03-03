<div align="center">

```
██████╗ ███████╗███████╗     █████╗ ██╗   ██╗██████╗  █████╗
██╔══██╗██╔════╝██╔════╝    ██╔══██╗██║   ██║██╔══██╗██╔══██╗
██████╔╝█████╗  █████╗      ███████║██║   ██║██████╔╝███████║
██╔══██╗██╔══╝  ██╔══╝      ██╔══██║██║   ██║██╔══██╗██╔══██║
██████╔╝███████╗███████╗    ██║  ██║╚██████╔╝██║  ██║██║  ██║
╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
```

#  Bee Aura Tech — Voice-Based ERP Support Assistant

### *"Speak to your ERP. Get answers instantly."*

[![Python](https://img.shields.io/badge/Python-3.10+-8b5cf6?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-ec4899?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-a855f7?style=for-the-badge)](https://groq.com)
[![Whisper](https://img.shields.io/badge/Whisper-large--v3-7c3aed?style=for-the-badge)](https://groq.com)


> **Intern Assessment — Use Case 3:** Voice-Based ERP Technical Support Assistant

</div>


##  Overview

**Bee Aura Tech ERP Voice Assistant** is an AI-powered, voice-first support system designed to automate first-level ERP support calls. Users can speak (or type) their ERP issue and receive instant, intelligent, voice-friendly responses — no human agent required for routine queries.

Built for the **Intern Assessment (Use Case 3)**, this prototype demonstrates how LLMs + speech technology can reduce human intervention in repetitive ERP support workflows.

---

##  Problem Statement

> ERP support teams spend enormous time handling repetitive voice-based queries — explaining errors, guiding navigation, troubleshooting configurations. Every minute a human agent spends on a routine call is a minute wasted.

**This system solves that by:**
-  Accepting natural spoken input from users
-  Understanding the ERP issue using a powerful LLM
-  Responding with clear, spoken troubleshooting steps
-  Maintaining conversation context for multi-turn interactions

---

##  Features

| Feature | Description |
|---|---|
|  **Voice Input** | Record audio directly in-browser via Streamlit's audio widget |
|  **Text Input** | Fallback text interface for non-voice scenarios |
|  **LLM Reasoning** | LLaMA 3.3 70B via Groq identifies module, issue type, and solutions |
|  **Voice Output** | gTTS converts AI responses to playable MP3 audio |
|  **Memory** | Full conversation history maintained within session |
|  **Multi-ERP Support** | SAP, Oracle Fusion, Microsoft Dynamics coverage |
|  **Multi-Module** | Finance, Inventory, HR, Procurement, CRM |

---

##  Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│                    (Streamlit — app.py)                         │
└────────────────┬────────────────┬───────────────────────────────┘
                 │                │
         Audio Input        Text Input
                 │                │
                 ▼                │
┌────────────────────────────┐    │
│     STT Module (stt.py)    │    │
│  Groq Whisper-large-v3     │    │
│  Audio → Transcribed Text  │    │
└──────────────┬─────────────┘    │
               │                  │
               └──────────┬───────┘
                          │
                          ▼ User Text
              ┌───────────────────────────┐
              │      LLM Module (llm.py)  │
              │   Groq LLaMA-3.3-70B      │
              │ + System Prompt (config)  │
              │ + Chat History (memory)   │
              │   → ERP Response Text     │
              └──────────────┬────────────┘
                             │
                             ▼ Response Text
              ┌──────────────────────────────┐
              │     TTS Module (tts.py)      │
              │      gTTS (Google TTS)       │
              │   Text → MP3 Audio Bytes     │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │   Streamlit UI Renders:      │
              │   • Chat bubble (text)       │
              │   • Audio player (voice)     │
              └──────────────────────────────┘
```

---

## Tech Stack

| Layer | Technology | Reason |
|---|---|---|
| **UI** | Streamlit 1.32 | Rapid prototyping, built-in audio widget |
| **STT** | Groq Whisper-large-v3 | Fast, accurate transcription via Groq's ultra-low latency API |
| **LLM** | LLaMA 3.3 70B (Groq) | State-of-the-art reasoning, free tier available, ~200 tok/s |
| **TTS** | gTTS (Google Text-to-Speech) | Simple, reliable, no API key needed |
| **Config** | python-dotenv | Secure credential management |

###  Why Groq?
Groq's LPU (Language Processing Unit) infrastructure delivers **~10x faster inference** than traditional GPU-based APIs, making it ideal for real-time voice applications where latency is critical.

---

##  Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/bee-aura-tech/erp-voice-assistant.git
cd erp-voice-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_LLM_MODEL=llama-3.3-70b-versatile
GROQ_STT_MODEL=whisper-large-v3-turbo
```

>  Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Run the App
```bash
streamlit run app.py
```

### 5. Open in Browser
```
http://localhost:8501
```

---

## 🔧 Configuration

All configuration lives in `config.py`:

```python
GROQ_LLM_MODEL  = "llama-3.3-70b-versatile"   # LLM model
GROQ_STT_MODEL  = "whisper-large-v3-turbo"     # STT model
SYSTEM_PROMPT   = "..."                         # ERP assistant persona
```

**For Streamlit Cloud deployment**, add secrets via the Streamlit Secrets UI — the app reads from `os.environ` automatically.

---

##  Project Structure

```
repo-main/
│
├── app.py              #  Main Streamlit UI — layout, routing, state management
├── llm.py              #  Groq LLM integration — chat completions with memory
├── stt.py              #  Speech-to-Text — Groq Whisper transcription
├── tts.py              #  Text-to-Speech — gTTS audio generation
├── config.py           #   Configuration — API keys, models, system prompt
│
├── requirements.txt    #  Python dependencies
├── packages.txt        #  System-level packages (for Streamlit Cloud)
├── .gitignore          #  Git ignore rules
│
├── README.md           #  This file
└── LLD.md              #  Low-Level Design document
```

---

##  How It Works

### Step-by-Step Flow

```
1. USER speaks into microphone  →  Browser captures WAV audio bytes

2. stt.py sends audio to Groq Whisper API
   └─ Returns: transcribed text string

3. llm.py builds message array:
   ├─ System prompt (ERP expert persona)
   ├─ Full chat history (conversation memory)
   └─ New user message

4. Groq LLaMA 3.3 70B processes and returns:
   ├─ Identified ERP module (SAP / Oracle / Dynamics)
   ├─ Issue type (Error / Config / How-to)
   ├─ Step-by-step troubleshooting (voice-friendly, no bullets)
   └─ Closing prompt for follow-up

5. tts.py converts response text → MP3 audio via gTTS

6. Streamlit renders:
   ├─ Chat bubble with response text
   └─ Audio player with autoplay
```

### Conversation Memory

The system maintains `chat_history` in `st.session_state`, passing the full history to every LLM call. This enables natural multi-turn conversations:

```
User:  "I can't post my vendor invoice"
Bot:   "Sounds like an SAP AP issue. Check posting period..."
User:  "The period is open but still failing"
Bot:   "In that case, check document type configuration..."  ← remembers context
```

---

##  Known Limitations

| Limitation | Impact | Notes |
|---|---|---|
| **gTTS requires internet** | TTS fails offline | Replace with offline TTS (Coqui, pyttsx3) for production |
| **No authentication** | Any user can access | Add OAuth/SSO for enterprise deployment |
| **Session memory only** | History lost on refresh | Add Redis/DB for persistent memory |
| **English only** | Non-English speakers excluded | Whisper supports 99 languages — extend config |
| **Max 300 tokens response** | Very long issues may be cut off | Increase limit or add streaming |
| **No RAG** | Answers based on LLM training only | Add knowledge base retrieval for accuracy |
| **Streamlit single-thread** | Not suitable for concurrent users at scale | Deploy with proper async backend |

---

##  Future Improvements

-  **Authentication** — SSO / enterprise login integration
-  **RAG Pipeline** — Connect ERP manuals, KB articles for grounded answers
-  **Multilingual** — Extend STT + TTS to support regional languages
-  **Analytics Dashboard** — Track issue types, modules, resolution rates
-  **Ticket Auto-Creation** — Unresolved issues auto-create support tickets
-  **WebRTC Integration** — Real phone call support via Twilio/Vonage
-  **Fine-tuning** — Train on company-specific ERP data for higher accuracy
-  **Persistent Memory** — Redis/PostgreSQL for cross-session conversation history

---

##  Scalability Considerations

| Concern | Current | Production Recommendation |
|---|---|---|
| **Concurrency** | Streamlit single-thread | FastAPI + async workers + Kubernetes |
| **LLM Latency** | ~1-2s (Groq LPU) | Add response streaming for perceived speed |
| **Audio Storage** | In-memory bytes | S3/GCS for large audio files |
| **Rate Limits** | Groq free tier (30 RPM) | Upgrade to paid tier + request queuing |
| **Monitoring** | None | Add Langsmith/Langfuse for LLM observability |
| **Cost** | ~$0 (free APIs) | Budget ~$0.001/query at scale with Groq paid |

---

<div align="center">

---

**🐝 Built with ❤️ by Bee Aura Tech**

*Enterprise AI Solutions — Making ERP Human Again*



</div>
