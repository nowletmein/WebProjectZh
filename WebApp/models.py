
#
from WebApp import db

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy.types import String, Integer


class Course(db.Model):
### Write your solution here!
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    code: Mapped[str] = mapped_column(String(6))
    students: Mapped[List["Student"]] = relationship(back_populates="course")
###    


class Student(db.Model):
### Write your solution here!
    
    __tablename__ = "student"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    neptun: Mapped[str] = mapped_column(String(6), unique=True)

    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))
    
    # visszahivatkozás a Course.students mezőre
    course: Mapped["Course"] = relationship(back_populates="students")
###    
