from flask import Blueprint, redirect, render_template, request, session
import sqlite3

app_home = Blueprint("home", __name__)

# page home
@app_home.route("/")
def page_home():
    if "username" not in session:
        return redirect("/login")
    else:
        return render_template("home/home.html")