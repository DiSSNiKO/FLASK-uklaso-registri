from unicodedata import name
from urllib.request import Request
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import registryvalidations

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'be52609c0bd9df4c2ae7f0f6'

db = SQLAlchemy(app)

class shopItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    desc = db.Column(db.String(length=150), nullable=False)
    status = db.Column(db.String(length=30), nullable=False, default="available")

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=50), nullable=False)

@app.route("/")
@app.route("/home")
def home_page():
    dbquery = shopItem.query.all()
    return render_template("home.html", listing=dbquery)

@app.route("/addlisting", methods=["POST"])
def addition():
    usefulData= request.get_json()
    print(usefulData)
    newitem = shopItem(name=usefulData["name"],price=usefulData["price"],desc=usefulData["desc"],status=usefulData["status"],)
    db.session.add(newitem)
    db.session.commit()
    return {"message":"success"}, 200

@app.route("/register", methods=["GET","POST"])
def registry():
    form = request.form
    if request.method=="POST":
        usernamelengthok = registryvalidations.lengthValid(5,form['user'])
        emaillengthok = registryvalidations.lengthValid(10,form['email'])
        isemail = registryvalidations.emailValid(form['email'])
        passwordlenok = registryvalidations.lengthValid(10,form['password'])
        if usernamelengthok and emaillengthok and isemail and passwordlenok:
            newuser = User(name=form['user'], email=form['email'], password=form['password'])
            db.session.add(newuser)
            db.session.commit()
    return render_template('form.html')
class owo():
    def rezistans():
        return "x"
    def vscode():
        return 50


if __name__=="__main__":
    app.run(debug=True)