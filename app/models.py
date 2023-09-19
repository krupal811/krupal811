from .extension import db

class Course(db.Model):
    id = db.Column (db.Integer, primary_key=True) 
    name = db.Column (db.String(50), unique=True)

    students = db.relationship("Student", back_populates="course")
    # employe = db.relationship("Employe", back_populates="course")

class Student(db.Model):
    id = db.Column (db.Integer, primary_key=True) 
    name = db.Column (db.String(50), unique=True) 
    course_id = db.Column (db.ForeignKey("course.id"))

    course = db.relationship("Course", back_populates="students")

class Employe(db.Model):
    id = db.Column (db.Integer, primary_key=True) 
    name = db.Column (db.String(50), unique=True)
    # course_id = db.Column (db.ForeignKey("course.id"))

    # course = db.relationship("Course", back_populates="employe")

