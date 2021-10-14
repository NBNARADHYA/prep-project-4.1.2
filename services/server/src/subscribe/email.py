from typing import List

from dotenv import dotenv_values
from fastapi import APIRouter, BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel, EmailStr
from starlette.requests import Request
from starlette.responses import JSONResponse

config_credentials = dotenv_values(".env")

email = APIRouter(tags=["email"])


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME=config_credentials["EMAIL"],
    MAIL_PASSWORD=config_credentials["PASS"],
    MAIL_FROM=config_credentials["EMAIL"],
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
)


template = """
weather = 22c
"""


@email.post("/api/subscribe/email")
async def email_subscribe(mail: EmailSchema) -> JSONResponse:

    # get user data later and generate jwt

    message = MessageSchema(
        subject="Test Subject",
        # List of recipients, as many as you can pass
        recipients=mail.dict().get("email"),
        body=template,
        subtype="html",
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
