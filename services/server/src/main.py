from fastapi import FastAPI
from subscribe.webhook import webhook
from subscribe.email import email

import uvicorn


app = FastAPI()
app.include_router(webhook)
app.include_router(email)
