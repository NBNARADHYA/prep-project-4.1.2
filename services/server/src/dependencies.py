from fastapi import Depends
from fastapi import Header
from fastapi import HTTPException


async def verify_token(x_token: str = Header(...)):
    return True


async def verify_token(token: str = Header("Authorization")):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Unauthorized token.")
