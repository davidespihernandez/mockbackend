from fastapi import APIRouter, HTTPException, status, Depends

from app.modules.mockers.users import UsersMocker
from app.modules.models.users import (
    SendLoginVerificationEmailRequest, LoginRequest, User, RegistrationResponse
)
from app.routers import auth_header

router = APIRouter()
mocker = UsersMocker()


@router.post("/customer/login/send-verification-email")
async def send_verification_email(request: SendLoginVerificationEmailRequest):
    return {}


@router.post("/customer/login")
async def login(request: LoginRequest):
    users_per_email = {
        user.email: user
        for token, user in mocker.objects.items()
    }
    if request.email not in users_per_email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user: User = users_per_email[request.email]
    return RegistrationResponse(authToken=user.token, customerId=1, userId=1)


@router.get("/users/user")
async def request_user(token: str = Depends(auth_header)):
    return mocker.get_detail(token)
