from pydantic import BaseModel


class segel(BaseModel):
    name: str
    is_active: bool

    class Config:
        orm_mode = True


class subject(BaseModel):
    name: str

    class Config:
        orm_mode = True


class person(BaseModel):
    first_name: str
    last_name: str
    segel_id: int

    class Config:
        orm_mode = True


class type(BaseModel):
    name: str

    class Config:
        orm_mode = True


class square(BaseModel):
    name: str
    type_id: int
    hours: int
    subject_id: int
    person_id: int
    notes: str

    class Config:
        orm_mode = True


