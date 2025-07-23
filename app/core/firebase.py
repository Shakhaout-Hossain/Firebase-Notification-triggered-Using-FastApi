import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebase-service-account.json")

# Avoid initializing more than once (useful with uvicorn reload)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
