from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import users

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
    app.include_router(users)

configure()

@app.get("/")
async def root():
    return {
        "message": "API SURVEYASIA", 
        "Authors":"Erik"
    }