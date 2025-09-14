from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from jose import jwt, JWTError
from fastapi import HTTPException, status
from typing import Dict
import os

SECRET_KEY= "your_secret_key"
ALGORITHM = "HS256"

EXCLUDED_PATHS = ["/","/login","/register"]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        if request.url.path in EXCLUDED_PATHS:
            response = await call_next(request)
            return response
    
        token = request.headers.get("Authorization")
        if not token:
            return JSONResponse(
                content={"detail" : "Not Authenticated"},
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        try:
            scheme,token_str = token.split(" ")
            if scheme.lower() != "bearer":
                raise ValueError("Invalid Authentication scheme")
            
            payload: Dict = jwt.decode(token_str,SECRET_KEY,algorithms=[ALGORITHM])
        except(ValueError, JWTError):
            return JSONResponse(
                content={"detail":"Invalid or expired token"},
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        response = await call_next(request)
        return response

