from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.auth_service import authenticate_user

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    user = authenticate_user(request.email, request.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": "fake-jwt-token"}
