from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Segel(Base):
    __tablename__ = 'segel'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_active = Column(Boolean)


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    segel_id = Column(Integer, ForeignKey("segel.id"))

class Type(Base):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Square(Base):
    __tablename__ = 'square'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_id = Column(Integer, ForeignKey("type.id"))
    hours = Column(Integer)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    person_id = Column(Integer, ForeignKey("person.id"))
    notes = Column(String)


