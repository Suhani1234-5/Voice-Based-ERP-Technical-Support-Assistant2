from groq import Groq
from config import GROQ_API_KEY, GROQ_LLM_MODEL, SYSTEM_PROMPT

client = None
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)

def get_erp_response(user_text, chat_history=[]):
    if not client:
        return "Error: GROQ_API_KEY is not set. Please add it to Streamlit Secrets."
    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        
        # Chat history add karo (memory ke liye)
        for msg in chat_history:
            messages.append(msg)
        
        # User ka message add karo
        messages.append({
            "role": "user", 
            "content": user_text
        })
        
        response = client.chat.completions.create(
            model=GROQ_LLM_MODEL,
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error getting response: {str(e)}"