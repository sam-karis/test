from flask import Flask
from hello import hello
import json

api = Flask(__name__)


@api.route("/")
def index():
    msg = hello("Sam Doe")
    return {"message": msg}


@api.route("/students")
def students():
    with open("names.json") as f:
        students = json.load(f)
    return students


@api.route("/addstudents/<name>/<uni>")
def add_students(name, uni):
    with open("names.json", 'r') as f:
        students = json.load(f)
        next_student = f'student_{str(len(students) + 1)}'
        students[next_student] = {}
        students[next_student]['name'] = name
        students[next_student]['uni'] = uni
    with open("names.json", 'w') as f:
        new_data = json.dumps(students, indent=4)
        f.write(new_data)
    return students
