from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )
    