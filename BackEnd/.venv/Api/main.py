from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Authentication.Register import router as Register

from Authentication.Login import router as login

from database import Base,engine

# create an object of FastPi
app = FastAPI()

# this allow api to communicate to react app 

origins = [
    "http://localhost:5173",   
    "http://127.0.0.1:5173"
]


app.add_middleware(
    
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = {"*"}  
)

# creat a table that inherit from Users model
Base.metadata.create_all(bind = engine)

# add routers
app.include_router(Register)
app.include_router(login)