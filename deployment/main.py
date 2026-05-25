from flask import Flask,render_template

# initializing the app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/reviews")
def review():
    return "Welcome to Your Review Page"

@app.route("/contact")
def contact():
    return "Welcome to contact Page"
# run the app
app.run()

