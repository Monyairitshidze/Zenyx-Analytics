from fastapi import APIRouter,Depends

from pydantic import BaseModel

from database import SessionLocal

from Models.users import Users

from sqlalchemy.orm import Session

router = APIRouter()

# define a function that takes adatabase sessioions
def get_database():

    db = SessionLocal()

    try:

        yield db

    finally:
      
      db.close()

# model that your login has to follow
class login(BaseModel):
   
   email : str
   password : str

# create a router
@router.post("/login")
def Login( current_user:login , db : Session = Depends(get_database)):
#    this method checks if the user esist and give then access tot the system or tell them to register or even return error if the login fails
   exixsting_user = db.query(Users).filter(Users.email == current_user.email , Users.password == current_user.password).first()

   if exixsting_user:
      
      return {"Message":"Login successfully"}
   
   return{"error":"Error try again"}