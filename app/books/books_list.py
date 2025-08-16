from pydantic import BaseModel

books = list()

class Book(BaseModel):

    id: int
    author: str
    title: str
    price: float
