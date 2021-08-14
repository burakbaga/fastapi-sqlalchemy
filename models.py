
from database import Base
from sqlalchemy import Column,String,Integer,Float

# student isminde bir tablo oluşturmak için 
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    age = Column(Integer)
    gpa = Column(Float)

    def __repr__(self) -> str:
        return f"<Name={self.name} Surname={self.surname} Age = {self.age} GPA = {self.gpa}>" 