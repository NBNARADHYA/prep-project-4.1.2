from typing import Optional

from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import JSONResponse

import services.server.schemas as schemas
from services.server.db import crud
from services.server.db.crud import get_db
from services.server.routers.oauth import starlette_config
from services.server.schemas import User
from services.server.verify import get_current_user

comment = APIRouter(tags=["comment"])
oauth = OAuth(starlette_config)


class Comment(BaseModel):
    comment: str
    email: str


@comment.post("/api/comments", response_model=User)
async def email_subscribe(
    db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    email = user.email
    user_comment = user.comment
    user_id = user.id
    item = Comment(user_comment, email)

    return crud.create_user_comment(db=db, item=item, user_id=user_id)
