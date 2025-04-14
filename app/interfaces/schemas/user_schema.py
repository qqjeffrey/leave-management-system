from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr
    name: str
    password: str

class RegisterResponse(BaseModel):
    email: EmailStr
    name: str
    message: str
