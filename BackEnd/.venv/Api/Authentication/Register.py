from fastapi import APIRouter,Depends

from pydantic import BaseModel

from database import SessionLocal,engine

from sqlalchemy.orm import Session

from Models.users import Users

# create an aobject of ApiRouter
router = APIRouter()

# create a function that create sessions 

def get_databae():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# create a model that define what has to be submited
class Register(BaseModel):
     
     fullName : str
     username:str
     email : str
     password : str
     confirmPassword : str

@router.post("/register")
def register_user(user:Register , db : Session = Depends(get_databae)):
# check if the user exists
    existing_user = db.query(Users).filter(Users.email == user.email).first()

    if existing_user:
        return {"Error" : "USER has already register"}
    
    if user.password != user.confirmPassword:
        return {"Error" : "Password do not match"}
    
 # add a new user if they dont exixst
    new_user = Users(

    fullName = user.fullName,
    username = user.username,
    email = user.email,
    password = user.password,
    confirmPassword = user.confirmPassword
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"Registration successfully"}
