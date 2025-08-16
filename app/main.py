from fastapi import FastAPI
from app.routes import books
import uvicorn

app = FastAPI()

app.include_router(books.router)

@app.get('/')
def read_root():

    response = {
        'message': "This is an API made possible by FastAPI!"
    }

    return response