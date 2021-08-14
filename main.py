# Student : Name - Surname - Age - GPA(5/5) 
# Öğrenci Ekle - Öğrenci Sil - Öğrencileri Listele - Öğrenci Bilgisi Güncelle - Öğrencileri Filtrele 

from os import stat
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import Optional,List

from sqlalchemy.util.langhelpers import monkeypatch_proxied_specials
from database import Base, Session
import models

app = FastAPI()

class Student(BaseModel):
    id : int 
    name : str
    surname : str
    age :int 
    gpa : float

    class Config:
        orm_mode = True

session = Session()


# Tüm öğrencileri getir  
@app.get("/students",response_model=List[Student],status_code = 200)
def get_all_student():
    students = session.query(models.Student).all()
    return students

# ID bilgisi verilen öğrenciyi getir 
@app.get("/students/{student_id}",response_model=Student,status_code=200)
def get_student(student_id:int):
    student = session.query(models.Student).filter(models.Student.id==student_id).first()
    return student

# Bilgileri girilen öğrenciyi db ye ekle 
@app.post("/students",response_model=Student,status_code=201)
def create_student(student:Student):
    new_student = models.Student(
        name = student.name,
        surname = student.surname,
        age = student.age,
        gpa = student.gpa
    )

    db_student = session.query(models.Student).filter(models.Student.name == student.name).first()

    if db_student is not None : 
        raise HTTPException(status_code=400,detail="This student already exist...")

    session.add(new_student)
    session.commit()

    return new_student
# ID si verilen öğrenciyi güncelle. 
@app.put("/students/{student_id}",response_model=Student,status_code=200)
def update_student(student_id : int,student:Student):
    student_up = session.query(models.Student).filter(models.Student.id==student_id).first()

    student_up.name = student.name
    student_up.surname = student.surname
    student_up.age = student.age
    student_up.gpa = student.gpa

    session.commit()
    return student_up

@app.delete("/students/{student_id}")
def delete_student(student_id : int):
    student_del = session.query(models.Student).filter(models.Student.id == student_id).first()
    if student_del is None:
        raise HTTPException(status_code=404,detail="Student NOT FOUND")

    session.delete(student_del)
    session.commit()

    return student_del
