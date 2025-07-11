# import time
# import random

# def send_sms(phone: str, message: str) -> dict:
#     time.sleep(1)

    
#     status = random.choice(["SENT", "FAILED"])

#     return {
#         "phone": phone,
#         "message": message,
#         "status": status,
#         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
#     }

import requests

MOBILE_SASA_TOKEN = "your_token."
MOBILE_SASA_SENDER = "MOBILESASA" 
MOBILE_SASA_URL = "https://api.mobilesasa.com/v1/send/message"

def send_sms(phone: str, message: str) -> dict:
    headers = {
        "Authorization": f"Bearer {MOBILE_SASA_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
    "phone": phone,
    "senderID": MOBILE_SASA_SENDER,
    "message": message
    }


    try:
        response = requests.post(MOBILE_SASA_URL, headers=headers, json=payload)
        response.raise_for_status()
        return {
            "status": "SENT",
            "response": response.json()
        }
    except requests.RequestException as e:
        return {
            "status": "FAILED",
            "error": str(e),
            "details": getattr(e.response, "text", None)
        }
