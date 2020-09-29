from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class SendLoginVerificationEmailRequest(BaseModel):
    email: EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    code: str


class RegistrationResponse(BaseModel):
    auth_token: str
    customer_id: int
    user_id: int


class User(BaseModel):
    token: Optional[str]
    title: str
    login: Optional[str]
    first_name: str
    last_name: str
    email: str
    address: Optional[str]
    postcode: Optional[str]
    town: Optional[str]
    country: Optional[str]
    phone: Optional[str]
    language: str
    birthday: Optional[date]
