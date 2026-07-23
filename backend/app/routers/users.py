from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.users import UserCreate, UserResponse
from app.database import get_db
from app.crud import users as user_crud


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("",
             response_model=UserResponse,
             status_code=status.HTTP_201_CREATED,
)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)) ->UserResponse:
    return user_crud.create_user(db, user_data)

@router.get("",
            response_model=list[UserResponse],
            status_code=status.HTTP_200_OK
)
def read_users(db: Session = Depends(get_db)) -> list[UserResponse]:
    return user_crud.get_users(db)
