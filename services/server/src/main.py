from fastapi import FastAPI
from services.server.src.subscribe.webhook import webhook
from services.server.src.subscribe.email import email

import uvicorn


app = FastAPI()
app.include_router(webhook)
app.include_router(email)
