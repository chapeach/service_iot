from flask import Blueprint, redirect, render_template, request, session
import sqlite3

app_form = Blueprint("form", __name__)

# page form test
@app_form.route("/form")
def page_form():
    return 'form'

# form repair request
@app_form.route("/form/RepairRequestForm")
def page_RepairRequestForm():
    return render_template('form/RepairRequestForm.html')

# form check status
@app_form.route("/form/CheckStatus")
def page_CheckStatusForm():
    return render_template('form/FormCheckStatus.html')