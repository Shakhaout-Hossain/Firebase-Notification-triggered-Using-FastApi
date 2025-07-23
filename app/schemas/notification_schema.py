from pydantic import BaseModel

class NotificationRequest(BaseModel):
    device_token: str
    title: str
    body: str
