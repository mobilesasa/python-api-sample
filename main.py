from fastapi import FastAPI, HTTPException
from models import SMSRequest
from sms import send_sms

app = FastAPI(title="SMS API")

@app.post("/send-sms")
def send_sms_endpoint(payload: SMSRequest):
    try:
        result = send_sms(payload.phone, payload.message)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
