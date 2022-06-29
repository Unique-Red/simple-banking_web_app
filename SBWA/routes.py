from flask import Flask, render_template
from SBWA import app

# GET \account_info\{accountNumber}
# GET \account_statement\{accountNumber}
# POST \deposit
# POST \withdrawal
# POST \create_account
# POST \login
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/withdrawal")
def withdrawal():
    return render_template("withdrawal.html")