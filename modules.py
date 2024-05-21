from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Создание базового класса для определения моделей
Base = declarative_base()

# Определение модели данных
class Play(Base):
    __tablename__ = 'plays'

    id = Column(Integer, primary_key=True)
    live  = Column(Integer)
    name  = Column(String)
# Подключение к базе данных
class PlayPydantic(BaseModel):
    id: int
    live: int
    name: str

SQLALCHEMY_DATABASE_URL = "sqlite:///./Plaeyrs.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
