from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.notification import router as notification_router

app = FastAPI(title="Firebase FCM FastAPI")
# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(notification_router, prefix="/api/v1/notification", tags=["Notification"])
