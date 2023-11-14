from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db, User
from schemas import User as UserScheme
from schemas import RegisterUser

app = FastAPI()


@app.get("/", response_model=List[UserScheme])
async def user_list(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.post("/", response_model=UserScheme)
async def create_user(user: RegisterUser, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user
