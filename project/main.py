from flask import Flask,render_template,request,jsonify


app = Flask(__name__)

# Temporary storage
feedback_list =[]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/feedback",methods =["GET","POST"])
def feedback():
    if request.method =="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")
        issue_type = request.form.get("issue_type")
        message = request.form.get("message")

        feedback_data={
            "name":name,
            "email":email,
            "course":course,
            "issue_type":issue_type,
            "message":message
        }

        feedback_list.append(feedback_data)

        return render_template ("success.html",data = feedback_data)
    return render_template("feedback.html")

@app.route("/all-feedback")
def all_feedback():
    return jsonify(feedback_list)

if __name__=="__main__":
    app.run(debug=True)
