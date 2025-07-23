# 🚀 FastAPI Firebase FCM Notification Service

This is a lightweight FastAPI application that sends push notifications to mobile devices using Firebase Cloud Messaging (FCM) via the Firebase Admin SDK.

---

## 📦 Features

- ✅ Send push notifications via FCM
- ✅ Uses Firebase Admin SDK for secure integration
- ✅ Asynchronous FastAPI endpoint
- ✅ Clean, modular code structure
- ✅ Python 3.10+ support

---

## 🛠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [Pydantic](https://docs.pydantic.dev/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

---

## 📁 Project Structure

.
├── app/
│ ├── main.py # App entry point
│ ├── core/
│ │ └── firebase.py # Firebase Admin SDK setup
│ ├── services/
│ │ └── fcm_service.py # FCM message logic
│ ├── api/
│ │ └── v1/notification.py # Notification endpoint
│ └── schemas/
│ └── notification_schema.py # Request model
├── firebase-service-account.json # 🔐 Firebase credentials (DO NOT COMMIT)
├── .gitignore
├── requirements.txt
└── README.md

---

## 🚀 Getting Started

### 1. Clone the repo

### 1. Clone the repo

```bash
git clone https://github.com/Shakhaout-Hossain/Firebase-Notification-triggered-Using-FastApi
cd Firebase-Notification-triggered-Using-FastApi
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Install dependencies 
```bash
pip install -r requirements.txt
```
### 4. Set up Firebase Admin SDK
. Go to the Firebase Console

. Navigate to:
. Project Settings → Service Accounts → Generate new private key

. Download the JSON file and save it as:
```bash
firebase-service-account.json
```
. firebase-service-account.json
. Ensure it's ignored in .gitignore

### ✅ Running the App
```bash
uvicorn app.main:app --reload
```
Visit:
http://localhost:8000/docs
to use the interactive Swagger UI.
### 📬 Sending a Notification
### Endpoint
```commandline
POST /api/v1/notification/send
```
### Sample JSON Body
```json
{
  "device_token": "YOUR_DEVICE_TOKEN_HERE",
  "title": "Hello!",
  "body": "This is a test notification from FastAPI"
}
```
### ⚠️ Important
1. 🔐 Never commit your .env or firebase-service-account.json

2. 📦 Use different credentials for dev, staging, and production

3. ✅ Secure endpoints using authentication if used in production

### 🧪 Coming Soon (Ideas)
1. Support for FCM topics and condition-based messaging
2. Add authentication with JWT
3. Dockerfile for containerization
4. CI/CD with GitHub Actions

### 📄 License
## MIT License. Use freely and modify for your needs.
```yaml
Would you like a matching `requirements.txt` and `Dockerfile` to complete your setup?
```