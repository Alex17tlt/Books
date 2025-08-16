from fastapi import APIRouter
from app.data.books_data import books
from app.models.models import Book

router = APIRouter()

@router.get('/list')
def list_books():

    return books

@router.post('/add')
def add_book(book: Book):

    books.append(book)

    response = {
        'status': 'Success',
        'book': book
    }

    return response

@router.get('/find/{id}')
def find_book(id: int):

    requested_book = None

    for i in books:

        if i.id == id:

            requested_book = i
            break


    if requested_book is not None:

        return requested_book
    else:

        return {"message": 'Book not found'}

@router.delete('/delete/{id}')
def delete_book(id: int):

    deleted = False

    for i in books:

        if i.id == id:

            books.remove(i)
            deleted = True
            break

    if deleted is True:

        response = {'message': "book deleted!"}
    else:
        response = {'message': "book not found!"}

    return response