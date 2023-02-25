import os
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    required_directories = ["content"]
    for directory in required_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)