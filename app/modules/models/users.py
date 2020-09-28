from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class SendLoginVerificationEmailRequest(BaseModel):
    email: EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    code: str


class RegistrationResponse(BaseModel):
    authToken: str
    customerId: int
    userId: int


class User(BaseModel):
    token: Optional[str]
    title: str
    login: Optional[str]
    firstName: str
    lastName: str
    email: str
    address: Optional[str]
    postcode: Optional[str]
    town: Optional[str]
    country: Optional[str]
    phone: Optional[str]
    language: str
    birthday: Optional[date]
