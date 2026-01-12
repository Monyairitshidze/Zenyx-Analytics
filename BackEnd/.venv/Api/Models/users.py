from database import Base

<<<<<<< HEAD
from sqlalchemy import Column,String,Integer
=======
from sqlalchemy import Column,String
>>>>>>> main

class Users(Base):

    __tablename__ = "users"

<<<<<<< HEAD
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column( String(225) , index=True)
    username = Column( String(225) , index=True)
=======
    fullName = Column( String(225) , index=True , primary_key=True)
>>>>>>> main
    email = Column( String(225) , index=True , unique=True)
    password = Column( String(225) )
    confirmPassword = Column( String(225) )