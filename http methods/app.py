# GET = Reads the data
# POST = Create new data
# PUT = Replace complete data
# PATCH = Updates partial/particular data
# DELETE = Removes the data

# API = Application Programming Interface

"""
# PROJECT:-
We are building a student course management system.

The system should allow us to:

1. View all students
2. View one student
3. Add a new student
4. Fully update a student
5. Partially update a student
6. Delete a student

For this we will create a Flask API.
"""

# from flask import Flask, jsonify


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return jsonify({
#         "message": "Welcome to student API",
#         "status": " success "
#     }) # response sent to client

# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": "Snehangshu",
        "email": "snehangshu@gmail.com",
        "course": "Data Science",
        "age": 23,
        "active": True,
    },
    {
        "id": "Ayan",
        "email": "ayan@gmail.com",
        "course": "Data Analyst",
        "age": 25,
        "active": True,
    },
]


def succes_response(
    message, data=None, status_code=200
):  # this function creats a standard succes response
    response = {"status": "success", "message": message}
    if data is not None:
        response["data"] = data

    return jsonify(response), status_code


def error_response(message, status_code=400):
    response = {"status": "error", "message": message}

    return jsonify(response), status_code


def find_student_by_id(student_id):  # this functions finds the student using student ID
    for student in students:
        if student["id"] == student_id:
            return student

        return None


def get_next_student_id():
    if len(students) == 0:
        return 1

    max_id = max(students["id"] for student in students)
    return max_id + 1

def validate_student_data(data,required_fields=True):#this function is vaildate student input data
    pass