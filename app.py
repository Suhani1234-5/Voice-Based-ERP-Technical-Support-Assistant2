import streamlit as st
from stt import transcribe_audio
from llm import get_erp_response
from tts import text_to_speech
import base64

st.set_page_config(
    page_title="Bee Aura Tech — ERP Voice Support",
    page_icon="🐝",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,700;0,800;1,400;1,700&family=Dancing+Script:wght@400;500;600;700&display=swap');

html, body { background: #f8f6fb !important; }

[data-testid="stAppViewContainer"] { background: #f8f6fb !important; }
[data-testid="stHeader"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
#MainMenu, footer { display: none !important; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── NAVBAR ── */
.navbar {
    background: #fff;
    border-bottom: 1px solid #ede8f5;
    padding: 14px 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.nb-logo { display: flex; align-items: center; gap: 8px; }
.nb-hex {
    width: 30px; height: 30px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
}
.nb-brand {
    font-size: 16px; font-weight: 700;
    color: #2d2b3d; letter-spacing: -0.3px;
}
.nb-brand span { color: #8b5cf6; }
.nb-right { display: flex; align-items: center; gap: 10px; }
.nb-status {
    display: flex; align-items: center; gap: 5px;
    font-size: 11px; color: #888;
}
.live-dot {
    width: 7px; height: 7px;
    background: #22c55e; border-radius: 50%;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%,100% { opacity:1; box-shadow: 0 0 0 0 rgba(34,197,94,0.4); }
    50% { opacity:.8; box-shadow: 0 0 0 4px rgba(34,197,94,0); }
}

/* ── HERO ── */
.hero-section {
    background: linear-gradient(180deg, #f8f6fb 0%, #efe8f8 50%, #e8dff5 100%);
    padding: 64px 48px 48px;
    text-align: center;
    position: relative;
    width: 100%;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem; font-weight: 800;
    color: #1a1a2e; line-height: 1.15;
    letter-spacing: -0.5px; margin-bottom: 4px;
}
.hero-title .gradient-text {
    background: linear-gradient(135deg, #a855f7, #ec4899);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-style: italic;
}
.hero-desc {
    font-size: 0.95rem; color: #888;
    line-height: 1.6; max-width: 600px;
    margin: 12px auto 28px;
}
.hero-tags {
    display: flex; flex-wrap: wrap;
    gap: 8px; justify-content: center;
}
.hero-tag {
    background: rgba(139,92,246,0.06);
    border: 1px solid rgba(139,92,246,0.15);
    color: #7c3aed;
    font-size: 12px; font-weight: 500;
    padding: 6px 18px; border-radius: 100px;
}
.hero-tag.active {
    background: rgba(139,92,246,0.12);
    border-color: rgba(139,92,246,0.3);
    color: #6d28d9; font-weight: 600;
}

/* ── STATS ── */
.stats-section {
    background: linear-gradient(180deg, #efe8f8 0%, #f3edfa 30%, #f8f6fb 100%);
    padding: 40px 48px 32px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    width: 100%;
}
.stat-card {
    background: #fff;
    border: 1px solid #ede8f5;
    border-radius: 20px;
    padding: 32px 16px 24px;
    box-shadow: 0 2px 16px rgba(139,92,246,0.05);
    text-align: center;
}
.stat-num {
    font-family: 'Dancing Script', cursive;
    font-size: 3.5rem; font-weight: 700;
    line-height: 1.1;
    background: linear-gradient(135deg, #c084fc, #e879a0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}
.stat-num sup {
    font-size: 1.6rem;
    background: linear-gradient(135deg, #c084fc, #e879a0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}
.stat-lbl {
    font-size: 11px; color: #bbb;
    font-weight: 600; letter-spacing: 2px;
    text-transform: uppercase; margin-top: 6px;
}

/* ── SECTION HEADERS ── */
.section-header {
    text-align: center;
    padding: 48px 48px 12px;
    width: 100%;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem; font-weight: 700;
    color: #1a1a2e; margin-bottom: 8px;
    font-style: italic;
}
.section-sub {
    font-size: 0.88rem; color: #aaa; line-height: 1.5;
}

/* ── CHAT ── */
.chat-wrap { padding: 16px 48px; width: 100%; }
.chat-card {
    background: #fff;
    border: 1px solid #ede8f5;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 2px 16px rgba(139,92,246,0.05);
    min-height: 120px;
}
.empty-chat { text-align:center; padding: 36px; }
.empty-icon { font-size: 40px; margin-bottom: 10px; }
.empty-lbl { font-size: 14px; color: #aaa; line-height: 1.6; }

.chat-header {
    display: flex; justify-content: space-between;
    align-items: center; margin-bottom: 16px;
    padding-bottom: 12px; border-bottom: 1px solid #f0ecf7;
}
.chat-agent { display: flex; align-items: center; gap: 10px; }
.chat-agent-icon {
    width: 32px; height: 32px;
    background: linear-gradient(135deg, #a855f7, #ec4899);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px;
}
.chat-agent-name { font-size: 14px; font-weight: 600; color: #2d2b3d; }
.chat-agent-sub  { font-size: 11px; color: #aaa; }
.chat-timestamp  { font-size: 11px; color: #ccc; }

.row-u { display:flex; justify-content:flex-end; margin-bottom:14px; }
.bub-u {
    background: linear-gradient(135deg, #a855f7, #7c3aed);
    color: #fff; font-size: 14px; font-weight: 500;
    padding: 12px 18px;
    border-radius: 16px 16px 4px 16px;
    max-width: 70%; line-height: 1.5;
    box-shadow: 0 4px 14px rgba(139,92,246,0.2);
}
.row-b { display:flex; gap:10px; margin-bottom:14px; align-items:flex-start; }
.b-av {
    width: 30px; height: 30px; flex-shrink:0;
    background: #f0ecf7; border-radius: 7px;
    display:flex; align-items:center; justify-content:center;
    font-size: 14px;
}
.bub-b {
    background: #faf8fd;
    border: 1px solid #ede8f5;
    color: #444; font-size: 14px;
    padding: 12px 18px;
    border-radius: 4px 16px 16px 16px;
    max-width: 70%; line-height: 1.65;
}

/* ── AUDIO ── */
.audio-wrap { padding: 0 48px; margin-bottom: 8px; width: 100%; }
.audio-card {
    background: #fff;
    border: 1px solid #ede8f5;
    border-left: 4px solid #a855f7;
    border-radius: 14px;
    padding: 16px 20px;
    box-shadow: 0 2px 12px rgba(139,92,246,0.05);
}
.audio-lbl {
    font-size: 10px; font-weight: 700;
    color: #a855f7; letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 10px;
}
audio { width: 100%; border-radius: 6px; }

/* ── COMMAND SECTION ── */
.command-section { padding: 0 48px; margin-bottom: 8px; width: 100%; }
.command-card {
    background: #fff;
    border: 1px solid #ede8f5;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 2px 16px rgba(139,92,246,0.05);
}
.inp-sec-lbl {
    font-size: 11px; font-weight: 600;
    color: #888; letter-spacing: 1px;
    text-transform: uppercase; margin-bottom: 8px;
    display: flex; align-items: center; gap: 6px;
    justify-content: center;
}

/* Widget overrides */
.stTextInput > div > div > input {
    background: #faf8fd !important;
    border: 1.5px solid #ede8f5 !important;
    border-radius: 10px !important;
    color: #333 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    padding: 14px 16px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #a855f7 !important;
    box-shadow: 0 0 0 3px rgba(168,85,247,0.1) !important;
    outline: none !important;
}
.stTextInput label { display:none !important; }

div[data-testid="stAudioInput"] {
    background: #faf8fd !important;
    border: 2px dashed #ddd6f0 !important;
    border-radius: 12px !important;
}

/* MAIN BUTTON */
.btn-wrap { padding: 0 48px 8px; }
.stButton > button {
    background: linear-gradient(135deg, #ec4899, #f472b6) !important;
    color: #fff !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important; font-weight: 700 !important;
    border: none !important; border-radius: 12px !important;
    padding: 16px 28px !important; width: 100% !important;
    box-shadow: 0 6px 20px rgba(236,72,153,0.25) !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #db2777, #ec4899) !important;
    box-shadow: 0 8px 28px rgba(236,72,153,0.4) !important;
    transform: translateY(-1px) !important;
}
.clr-wrap .stButton > button {
    background: #faf8fd !important; color: #999 !important;
    border: 1px solid #ede8f5 !important;
    box-shadow: none !important; font-size: 13px !important;
}

/* FOOTER */
.foot {
    text-align: center; padding: 24px;
    margin-top: 24px; font-size: 12px; color: #bbb;
    letter-spacing: 0.5px;
}
.foot a { color: #a855f7; text-decoration: none; font-weight: 600; }
.foot .foot-links { margin-top: 4px; font-size: 11px; color: #ccc; }
</style>
""", unsafe_allow_html=True)

# ── NAVBAR ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
    <div class="nb-logo">
        <div class="nb-hex">🐝</div>
        <div class="nb-brand"><span>Bee</span> Aura Tech</div>
    </div>
    <div class="nb-right">
        <div class="nb-status">
            <div class="live-dot"></div>
            AI Online
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-title">Intelligent Voice AI for<br><span class="gradient-text">Enterprise ERP</span></div>
    <div class="hero-desc">
        Seamlessly command, query, and troubleshoot your entire business infrastructure
        using natural voice interactions. The future of enterprise management is here.
    </div>
    <div class="hero-tags">
        <span class="hero-tag active">Invoices</span>
        <span class="hero-tag active">ERP</span>
        <span class="hero-tag active">Supply Chain</span>
        <span class="hero-tag">Inventory</span>
        <span class="hero-tag">CRM</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SESSION ────────────────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages_display" not in st.session_state:
    st.session_state.messages_display = []
if "last_audio" not in st.session_state:
    st.session_state.last_audio = None

# ── STATS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-section">
    <div class="stat-card">
        <div class="stat-num">99.7<sup>%</sup></div>
        <div class="stat-lbl">ACCURACY RATE</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">50ms</div>
        <div class="stat-lbl">RESPONSE TIME</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">10K+</div>
        <div class="stat-lbl">QUERIES / DAY</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ENTERPRISE-GRADE INTELLIGENCE ─────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <div class="section-title">Enterprise-Grade Intelligence</div>
    <div class="section-sub">Complex multi-system operations that were never this easy before</div>
</div>
""", unsafe_allow_html=True)

# ── CHAT ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="chat-wrap"><div class="chat-card">', unsafe_allow_html=True)
st.markdown("""
<div class="chat-header">
    <div class="chat-agent">
        <div class="chat-agent-icon">🐝</div>
        <div>
            <div class="chat-agent-name">Bee AI Assistant</div>
            <div class="chat-agent-sub">● Active</div>
        </div>
    </div>
    <div class="chat-timestamp">⏱ Today's Session</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.messages_display:
    st.markdown("""
    <div class="empty-chat">
        <div class="empty-icon">🐝</div>
        <div class="empty-lbl">Hello! I'm your ERP Support AI.<br>Speak or type your issue below to get started.</div>
    </div>""", unsafe_allow_html=True)
else:
    for msg in st.session_state.messages_display:
        if msg["role"] == "user":
            st.markdown(f'<div class="row-u"><div class="bub-u">🎤 {msg["content"]}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="row-b"><div class="b-av">🐝</div><div class="bub-b">{msg["content"]}</div></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── AUDIO ──────────────────────────────────────────────────────────────────────
if st.session_state.last_audio:
    b64 = base64.b64encode(st.session_state.last_audio).decode()
    st.markdown(f"""
    <div class="audio-wrap">
        <div class="audio-card">
            <div class="audio-lbl"> Voice Response</div>
            <audio autoplay controls>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        </div>
    </div>""", unsafe_allow_html=True)

# ── COMMAND YOUR ENTERPRISE ───────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <div class="section-title">Command Your Enterprise</div>
    <div class="section-sub">Speak or type your query to interact with your ERP</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="command-section"><div class="command-card">', unsafe_allow_html=True)
col_audio, col_text = st.columns(2, gap="medium")
with col_audio:
    st.markdown('<div class="inp-sec-lbl"> Voice Input</div>', unsafe_allow_html=True)
    audio_input = st.audio_input("mic", label_visibility="collapsed")
with col_text:
    st.markdown('<div class="inp-sec-lbl"> Text Input</div>', unsafe_allow_html=True)
    text_input = st.text_input("txt", label_visibility="collapsed",
        placeholder="e.g., 'Show me Q3 revenue'")
st.markdown('</div></div>', unsafe_allow_html=True)

# ── BUTTON ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="btn-wrap">', unsafe_allow_html=True)
submit = st.button("Analyze with Bee AI ", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── PROCESS ────────────────────────────────────────────────────────────────────
if submit:
    user_text = ""
    if audio_input is not None:
        with st.spinner("Transcribing..."):
            user_text = transcribe_audio(audio_input.read())
        st.success(f" Heard: *{user_text}*")
    elif text_input.strip():
        user_text = text_input.strip()
    else:
        st.warning(" Please speak or type your ERP issue.")

    if user_text:
        with st.spinner("Analyzing your ERP issue..."):
            response = get_erp_response(user_text, st.session_state.chat_history)
        st.session_state.chat_history += [
            {"role": "user", "content": user_text},
            {"role": "assistant", "content": response}
        ]
        st.session_state.messages_display += [
            {"role": "user", "content": user_text},
            {"role": "assistant", "content": response}
        ]
        with st.spinner(" Generating voice..."):
            st.session_state.last_audio = text_to_speech(response)
        st.rerun()

# ── CLEAR ──────────────────────────────────────────────────────────────────────
if st.session_state.messages_display:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="btn-wrap clr-wrap">', unsafe_allow_html=True)
    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.messages_display = []
        st.session_state.last_audio = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="foot">
    🐝 <a href="#">Bee Aura Tech</a>
    <div class="foot-links">© 2024 Bee Aura Tech. All Rights Reserved. Enterprise AI Solutions</div>
</div>
""", unsafe_allow_html=True)
