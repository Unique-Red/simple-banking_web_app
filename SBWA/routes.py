from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask.globals import request
from SBWA import app
from .models import Bank
from werkzeug.security import generate_password_hash, check_password_hash
import random

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
        accountNumber = request.form["accountNumber"]
        accountPassword = request.form["accountPassword"]

        if str(accountNumber) in users and users[str(accountNumber)] == accountPassword:
            session["user"] = str(accountNumber)

            user = Bank(session["user"], str(accountNumber))
            print (user.show_details())

            flash("Login successful")
            return redirect(url_for("home"))
        elif users[str(accountNumber)] != accountPassword:
            flash("Incorrect credentials", category="error")
        else:
            flash("Account doesn't exist", category="error")
            return render_template("login.html")


    return render_template("login.html")

@app.route("/create_account", methods=["GET", "POST"])
def register():
    global user
    if request.method == "POST":
        accountName = request.form.get("accountName")
        initial_deposit = request.form.get("initial_deposit")
        accountPassword = request.form.get("accountPassword")
        accountNumber = random.randint(1000000000, 9999999999)
        # red = Bank(accountName, random.randint(1000000000, 9999999999))
        if accountName in users:
            flash("Account name already in use", category="error")
            return render_template("register.html")
        elif int(initial_deposit) < 500:
            flash("Initial deposit should be minimum #500:00", category="error")
            return render_template("register.html")

        else:
            accountPassword = request.form["accountPassword"]
            users[str(accountNumber)] = accountPassword
            user = Bank(accountName, accountNumber)
            user.initial_deposit(initial_deposit)
            flash("User created.")
            print(users)
            print(user.show_details())
            return  "This is your account number: {}. Save it somewhere as you will subsequently use it to login. Now go to '/login'".format(accountNumber)
            # return redirect(url_for("login"))
    else:
        return render_template("register.html")


@app.route("/account_number", methods=["GET", "POST"])
def account_number():
    accountName = Bank(accountName)
    return render_template("account.html", accountName=accountName)


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        deposit = request.form["deposit"]
        user.deposit(deposit)
        print(user.show_details())
    return render_template("deposit.html")

@app.route("/withdrawal", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        amount = request.form["withdraw"]
        user.withdraw(amount)
        print(user.show_details())
    return render_template("withdrawal.html")
