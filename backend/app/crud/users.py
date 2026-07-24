from fastapi import HTTPException, status

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate


def create_user(db: Session, user_data: UserCreate) -> User:
    user = User(
        email=user_data.email,
        name=user_data.name,
        password=user_data.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session) -> list[User]:
    statement = select(User).order_by(User.id)
    return list(db.scalars(statement).all())

def get_user(user_id: int, db: Session) ->  User:
    return db.get(User, user_id)

def update_user(user_id: int, user_data: UserUpdate, db: Session) -> User:
    user = db.get(User, user_id)
    if user is None:
        return None
    
    if user_data.email is not None:
        user.email = user_data.email

    if user_data.name is not None:
        user.name = user_data.name

    if user_data.password is not None:
        user.password = user_data.password

    db.commit()
    db.refresh(user)
    
    return user

def delete_user(user_id: int, db: Session) -> None:
    user = db.get(User, user_id)

    if user is None:
        return None
    db.delete(user)
    db.commit()
    return user
