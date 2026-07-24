from pydantic import BaseModel, ConfigDict, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name: str | None = None
    password: str | None = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str | None = None

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    name: str | None = None
    password: str | None = None