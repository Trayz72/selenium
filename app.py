from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template("login.html", username=username, password=password)

if __name__ == "__main__":
    app.run(debug=True,port=5050)
