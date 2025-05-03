
from sqlalchemy import (
    Column, String, Integer,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    # cascade: all, delete-orphan.
    # When delete a user, also delete task item associated with the user.
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    description = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

