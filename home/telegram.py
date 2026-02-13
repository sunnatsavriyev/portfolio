import requests

TOKEN = "8351295778:AAHObNWtDHLRm_YpX_pdv23JCoEt8BYqTXI"
ADMIN_IDS = [1948824452]

def send_to_admins(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    for admin in ADMIN_IDS:
        try:
            requests.post(url, json={
                "chat_id": admin,
                "text": text
            }, timeout=5)
        except Exception as e:
            print("Telegram error:", e)
