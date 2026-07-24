from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.users import UserCreate, UserResponse, UserUpdate
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


@router.get("/{user_id}",
            response_model=UserResponse,
            status_code=status.HTTP_200_OK
)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    user = user_crud.get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")
    return user


@router.patch("/{user_id}",
            response_model=UserResponse,
            status_code=status.HTTP_200_OK,
)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)) -> UserResponse:
    return user_crud.update_user(user_id, user_data, db)

@router.delete(
            "/{user_id}",
            response_model=None,
            status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> None:
    if user_crud.delete_user(user_id, db) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")
