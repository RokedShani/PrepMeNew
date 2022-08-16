import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import segel as SchemaSegel
from schema import subject as SchemaSubject

from schema import segel
from schema import subject

from models import Person as ModelPerson
from models import Type as ModelType
from models import Square as ModelSquare
from models import Segel as ModelSegel
from models import Subject as ModelSubject

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get("/")
async def root():
    return {"message": "shaked"}


# @app.post('/book/', response_model=SchemaBook)
# async def book(book: SchemaBook):
#     db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)
#     db.session.add(db_book)
#     db.session.commit()
#     return db_book


@app.get('/segel')
async def segel():
    segel = db.session.query(ModelSegel).all()
    return segel


# @app.post('//', response_model=SchemaAuthor)
# async def author(author: SchemaAuthor):
#     db_author = ModelAuthor(name=author.name, age=author.age)
#     db.session.add(db_author)
#     db.session.commit()
#     return db_author


@app.get('/subject')
async def subject():
    subject = db.session.query(ModelSubject).all()
    return subject

@app.get('/person')
async def person():
    person = db.session.query(ModelPerson).all()
    return person

@app.get('/type')
async def type():
    type = db.session.query(ModelType).all()
    return type

@app.get('/square')
async def square():
    square = db.session.query(ModelSquare).all()
    return square

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
