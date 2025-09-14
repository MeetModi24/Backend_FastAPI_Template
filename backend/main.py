from fastapi import FastAPI
from controllers import users
from middleware.auth import AuthMiddleware
from middleware.logger import LogRequestMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

app = FastAPI()

origins = ["http://localhost:3000"]


app.add_middleware(AuthMiddleware)
app.add_middleware(LogRequestMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)

@app.get('/')
def health():
    return {"message":"Hello, FastAPI"}

@app.get('/protected')
async def protected_route(request:Request): 
    return {"message":"You are a valid user"}




