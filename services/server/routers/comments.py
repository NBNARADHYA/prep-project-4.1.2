from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional

from services.server.db.crud import get_db
from starlette.requests import Request
from sqlalchemy.orm import Session
from authlib.integrations.starlette_client import OAuth, OAuthError

from services.server.db import crud

from services.server.routers.oauth import starlette_config
from starlette.responses import JSONResponse

from services.server.schemas import Comment

comment = APIRouter(
    tags=["comment"]
)
oauth = OAuth(starlette_config)


@comment.post('/api/comments')
async def email_subscribe(req: Request, db: Session = Depends(get_db)):
    try:
        access_token = await oauth.google.authorize_access_token(req)
    except OAuthError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    user_data = await oauth.google.parse_id_token(req, access_token)
    email = user_data['email']
    user_comment = user_data['comment']
    user_id = user_data['id']
    item = Comment(user_comment, email)

    return crud.create_user_comment(db=db, item=item, user_id=user_id)
