import uvicorn
from fastapi import FastAPI

from services.server.src.subscribe.email import email
from services.server.src.subscribe.webhook import webhook

app = FastAPI()
app.include_router(webhook)
app.include_router(email)
