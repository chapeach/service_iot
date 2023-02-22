from flask import Blueprint, redirect, render_template, request, session
import sqlite3

app_service = Blueprint("service", __name__)

# page customer by code
@app_service.route("/service")
def page_service():
    return render_template("service/service.html")

# page service code
@app_service.route("/service/SV-001")
def page_service_code():
    return render_template("service/sv-001.html")