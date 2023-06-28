from flask import Flask, render_template, request, flash,url_for

app = Flask(__name__)
app.secret_key = "26456134565644646d5454s454s154w555q151d"


@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi, " + str(request.form.get('input_text', False)) + ", nice to see you!")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
