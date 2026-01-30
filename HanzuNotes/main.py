from fastapi import FastAPI
from . import models
from .database import engine
from .router import notes
from fastapi.middleware.cors import CORSMiddleware

hanzu = FastAPI()

hanzu.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your Flutter app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

hanzu.include_router(notes.router)

@hanzu.get('/posts')
def getData():
    return 