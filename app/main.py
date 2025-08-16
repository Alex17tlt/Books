from fastapi import FastAPI
from books.books_list import Book, books

app = FastAPI()

@app.get('/')
def read_root():

    response = {
        'message': "This is an API made possible by FastAPI!"
    }

    return response

@app.post('/book')
def add_book(book: Book):

    books.append(book)

    return book