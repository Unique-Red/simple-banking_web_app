from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask.globals import request
from SBWA import app
from .models import Bank
from werkzeug.security import generate_password_hash, check_password_hash

# GET \account_info\{accountNumber}
# GET \account_statement\{accountNumber}
# POST \deposit
# POST \withdrawal
# POST \create_account
# POST \login

users = {}
print(users)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    global user
    if request.method == "POST":
        accountName = request.form["accountName"]
        accountPassword = request.form["accountPassword"]

        if accountName in users and users[accountName] == accountPassword:
            session["user"] = accountName

            user = Bank(session["user"])
            print (user.show_details())

            flash("Login successful")
            return redirect(url_for("home"))
        else:
            flash("Account doesn't exist", category="error")
            return render_template("login.html")


    return render_template("login.html")

@app.route("/create_account", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        accountName = request.form.get("accountName")

        if accountName in users:
            flash("Account name already in use")
            return render_template("register.html", category="error")
        else:
            accountPassword = request.form["accountPassword"]
            users[accountName] = accountPassword
            flash("User created")
            print(users)
            return redirect(url_for("login"))
    else:
        return render_template("register.html")

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        amount = request.form["deposit"]
        user.deposit(amount)
        print(user.show_details())
    return render_template("deposit.html")

@app.route("/withdrawal", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        amount = request.form["withdraw"]
        user.withdraw(amount)
        print(user.show_details())
    return render_template("withdrawal.html")