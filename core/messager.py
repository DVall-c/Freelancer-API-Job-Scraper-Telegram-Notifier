import requests
from core.settings import BOT_TOKEN, CHAT_ID

# ==========================================
# Sending messages to Telegram is a separate concern
# so we put it in its own file for better organization and separation
# ==========================================

def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    
    try:
        # we send the message to Telegram using the Bot API, and we check for any errors in the response
        response = requests.post(url, data=data)
        response.raise_for_status()
        print("[Telegram] Just sending another job for you")
        # we could also check the response content for Telegram's own error messages, 
        # but for simplicity we'll just rely on HTTP status codes here
    except Exception as e:
        print(f"[Telegram] Sending fail...: {e}")