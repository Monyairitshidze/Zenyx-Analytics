from fastapi import APIRouter

from database import SessionLocal

# create an aobject of ApiRouter
router = APIRouter()

# create a function that create sessions 

def get_databae():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()