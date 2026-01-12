from database import Base

from sqlalchemy import Column,String,Integer

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column( String(225) , index=True)
    username = Column( String(225) , index=True)
    email = Column( String(225) , index=True , unique=True)
    password = Column( String(225) )
    confirmPassword = Column( String(225) )