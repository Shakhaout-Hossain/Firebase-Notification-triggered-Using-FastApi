from fastapi import FastAPI
from app.api.v1.notification import router as notification_router

app = FastAPI(title="Firebase FCM FastAPI")

app.include_router(notification_router, prefix="/api/v1/notification", tags=["Notification"])
