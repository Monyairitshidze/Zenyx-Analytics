from database import Base

from sqlalchemy import Column,String

class Users(Base):

    __tablename__ = "users"

    fullName = Column( String(225) , index=True , primary_key=True)
    email = Column( String(225) , index=True , unique=True)
    password = Column( String(225) )
    confirmPassword = Column( String(225) )