from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Database_Url = "mysql+pymysql://root:root@localhost:3306/zenyxdev"

# create connection between pyhton appp and database
engine = create_engine(Database_Url)

# create sessions
SessionLocal = sessionmaker(bind=engine)

# its used to define tables of database using python classes
Base = declarative_base()