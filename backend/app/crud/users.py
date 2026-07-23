from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate


def create_user(db: Session, user_data: UserCreate) -> User:
    user = User(email=user_data.email)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session) -> list[User]:
    statement = select(User).order_by(User.id)
    return list(db.scalars(statement).all())