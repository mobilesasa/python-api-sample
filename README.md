# SMS API Service

A simple FastAPI-based service for sending SMS messages using the MobileSasa API.

## Features
- Exposes a REST API endpoint to send SMS messages.
- Validates input using Pydantic models.
- Integrates with the MobileSasa SMS gateway.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [License](#license)

---

## Requirements
- Python 3.9+
- See `requirements.txt` for Python dependencies:
  - fastapi
  - uvicorn
  - pydantic

---

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd send_sms
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration
The SMS sending logic uses the MobileSasa API. You must set your MobileSasa API token in `sms.py`:

```
MOBILE_SASA_TOKEN = "your_token."
```

- Replace `your_token.` with your actual MobileSasa API token.
- You can also change the sender ID and API URL if needed:
  - `MOBILE_SASA_SENDER` (default: `MOBILESASA`)
  - `MOBILE_SASA_URL` (default: `https://api.mobilesasa.com/v1/send/message`)

---

## Usage
### Running the API server
Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000` by default.

### Sending an SMS
Send a POST request to `/send-sms` with a JSON payload:

```
POST /send-sms
Content-Type: application/json

{
  "phone": "+12345678901",
  "message": "Hello from FastAPI!"
}
```

#### Example using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/send-sms" \
     -H "Content-Type: application/json" \
     -d '{"phone": "+12345678901", "message": "Hello from FastAPI!"}'
```

#### Example response:
```
{
  "status": "success",
  "data": {
    "status": "SENT",
    "response": { ... }  // Response from MobileSasa API
  }
}
```

If the SMS fails to send, the response will include an error message and details.

---

## API Reference
### POST `/send-sms`
- **Request Body:**
  - `phone` (string, required): Recipient's phone number (10-15 characters)
  - `message` (string, required): Message content (1-160 characters)
- **Response:**
  - `status`: "success" or "error"
  - `data`: Contains the result from the SMS sending logic

#### Request Model Example
```
{
  "phone": "+12345678901",
  "message": "Test message"
}
```

#### Response Model Example
```
{
  "status": "success",
  "data": {
    "status": "SENT",
    "response": { ... }
  }
}
```

---

## Project Structure
```
send_sms/
├── main.py         # FastAPI app and API endpoint
├── models.py       # Pydantic models for request validation
├── sms.py          # SMS sending logic (MobileSasa integration)
├── requirements.txt# Python dependencies
├── README.md       # Project documentation
├── .gitignore      # Git ignore rules
└── venv/           # Python virtual environment (ignored by git)
```

- **main.py**: Defines the FastAPI app and the `/send-sms` endpoint. Handles incoming requests and delegates SMS sending to `sms.py`.
- **models.py**: Contains the `SMSRequest` Pydantic model, which validates the phone number and message fields.
- **sms.py**: Implements the `send_sms` function, which sends SMS messages via the MobileSasa API. Configure your API token and sender ID here.
- **requirements.txt**: Lists all Python dependencies required to run the project.
- **.gitignore**: Specifies files and directories to be ignored by git (e.g., `venv/`, `.DS_Store`, etc.).

---

## License
This project is licensed under the MIT License. 