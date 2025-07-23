from firebase_admin import messaging
from app.core import firebase  # ensures Firebase is initialized

async def send_fcm_notification(device_token: str, title: str, body: str):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=device_token,
    )

    try:
        response = messaging.send(message)
        return {"status": "success", "message_id": response}
    except Exception as e:
        return {"status": "error", "details": str(e)}
