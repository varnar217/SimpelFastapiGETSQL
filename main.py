from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from modules import SessionLocal, engine, Play, Base,PlayPydantic
# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)


# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Инициализация FastAPI
app = FastAPI()
# Маршрут для получения данных из базы данных
@app.get("/plays/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Play).filter(Play.id == user_id).first()
    logging.info(f"User with ID {user_id} retrieved")
    return user
# Маршрут для получения данных из базы данных
@app.get("/plays23")
async def read_all_user(db: Session = Depends(get_db)):
    users = db.query(Play).all()
    logging.info("All users retrieved")
    return users


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8084)
