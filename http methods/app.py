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

from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to student API",
        "status": " success "
    })

if __name__=="__main__":
    app.run(debug=True)