from fastapi import APIRouter
from app.schemas.notification_schema import NotificationRequest
from app.services.fcm_service import send_fcm_notification

router = APIRouter()

@router.post("/send")
async def send_notification(payload: NotificationRequest):
    return await send_fcm_notification(
        device_token=payload.device_token,
        title=payload.title,
        body=payload.body
    )
