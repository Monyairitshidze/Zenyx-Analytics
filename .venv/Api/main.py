from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# create an object of FastPi
app = FastAPI()

# this allow api to communicate to react app 
app.add_middleware(
    
    CORSMiddleware,
    allow_origins = ["http://localhost:5173/"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = {"*"}  
)