from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users_register import register
from routes.users_login import login
from routes.users_profile import profile
from routes.users_username import username

app = FastAPI()

def cors_headers(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
        )
    return app

def configure():
    app.include_router(register)
    app.include_router(login)
    app.include_router(profile)
    app.include_router(username)


configure()

@app.get("/")
async def root():
    return {
        "message": "API SURVEYASIA", 
        "Authors":"Erik"
    }