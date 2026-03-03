# Bee Aura Tech: Voice-Based ERP Technical Support Assistant

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat-square&logo=streamlit)
![Groq](https://img.shields.io/badge/Inference-Groq_LPU-f5f5f5?style=flat-square)
![Llama3](https://img.shields.io/badge/LLM-Llama_3-0668E1?style=flat-square&logo=meta)
![Whisper](https://img.shields.io/badge/STT-Whisper_v3-black?style=flat-square)

**Bee Aura Tech** is a high-performance, voice-first AI assistant designed for enterprise ERP troubleshooting. Built for the modern workforce, it allows users to interact with complex ERP modules (SAP, Oracle, Microsoft Dynamics) through natural language and voice commands, delivering instant, actionable solutions.

---

##  Key Features

- **Multimodal Interaction**: Seamlessly switch between voice input and text queries.
- **Enterprise-Grade Reasoning**: specialized in ERP modules like Finance, Supply Chain, HR, and Procurement.
- **Ultra-Low Latency**: Powered by Groq's LPU™ technology for near-instant STT and LLM inference.
- **Natural Voice Synthesis**: High-quality speech responses using neural TTS engines.
- **Premium UX**: Modern, responsive dashboard with real-time status monitoring.

---

##  Technical Architecture

The system follows a modular, decoupled architecture focused on high inference throughput:

1.  **Speech-to-Text (STT)**: Transcribes user audio using `whisper-large-v3` on Groq.
2.  **LLM Inference**: Processes intent and generates ERP solutions via `Llama-3-70b`.
3.  **Text-to-Speech (TTS)**: Synthesizes responses into voice using `gTTS`.
4.  **Frontend**: Built with Streamlit, utilizing custom CSS for a professional enterprise feel.

Detailed design specifications can be found in [LLD.md](./LLD.md).

---

##  Getting Started

### Prerequisites

- Python 3.9+
- A [Groq API Key](https://console.groq.com/)
- FFmpeg installed on your system (for audio processing)

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Voice-Based-ERP-Technical-Support-Assistant2
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

### Running the Application

Launch the Streamlit dashboard:
```bash
streamlit run app.py
```



*Developed for Enterprise ERP Excellence.*
