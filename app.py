from flask import Flask,redirect,url_for, render_template, request

app = Flask(__name__)

data = {1:"Fraise",2:"Tomate",3:"test"}

@app.route('/hello/<int:id>')
def hello_world(id):
    return f"{data[id]}"
    # return render_template("test.html", name=id)

@app.route('/user/<name>')
def hello_user(name):
    if name=="admin":
        return redirect(url_for("hello_world", id=1))
    
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        return f"hello {request.form['user']}"
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)