from flask_restx import fields
from .extension import api

student_model = api.model("Student", {
    "id": fields. Integer,
    "name": fields.String,
    # "course": fields.Nested(course_model)
    #"students"
})

employe_model = api.model("Employe", {
    "id": fields. Integer,
    "name": fields.String,
})

image_Edit_model = api.model("ImageEdit", {
    "id": fields. Integer,
    "name": fields.String,
})

course_model = api.model("Course", {
    "id": fields. Integer,
    "name": fields.String,
    "students": fields.List(fields.Nested(student_model)),
})

course_input_model = api.model("CourseInput", { 
    "name": fields.String,
})

student_input_model = api.model("StudentInput", { 
    "name": fields.String,
    "course_id": fields.Integer,
})

employe_input_model = api.model("EmployeInput", { 
    "name": fields.String,
    # "course_id": fields.Integer,
})

image_Edit_model = api.model("ImageEdit", {
    "img": fields.String(description="Base64-encoded image data"),
})

image_edit_input_model = api.model("ImageEditInput", { 
    "img": fields.String,
})

