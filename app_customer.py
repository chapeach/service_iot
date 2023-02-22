from flask import Blueprint, redirect, render_template, request, session
import sqlite3

app_customer = Blueprint("customer", __name__)

# page add code customer
@app_customer.route("/customer/add_code")
def page_add_customer():
    con = sqlite3.connect("db/db.db")
    cur = con.cursor()
    sql = 'select * from tb_customer order by no desc'
    curs = cur.execute(sql)
    data = curs.fetchall()
    return render_template("customer/add_customer.html", data=data)

# fn add customer
@app_customer.route("/customer/add_code/fn_add_customer", methods=["POST"])
def fn_add_customer():
    id_code = request.form["id_code"]
    con = sqlite3.connect("db/db.db")
    cur = con.cursor()
    sql = 'insert into tb_customer (id_code) values ("{}")'.format(id_code)
    curs = cur.execute(sql)
    con.commit()
    return redirect("/customer/add_code")

# page customer list
@app_customer.route("/customer/list")
def page_customer_list():
    con = sqlite3.connect("db/db.db")
    cur = con.cursor()
    sql = 'select * from tb_customer order by no desc'
    curs = cur.execute(sql)
    data = curs.fetchall()
    return render_template("customer/customer_list.html", data=data)

# page customer by code
@app_customer.route("/customer/view/RETRO-001")
def page_customer_view_code():
    return render_template("customer/RETRO-001.html")

# page Service Request by code
@app_customer.route("/customer/ServiceRequest/RETRO-001")
def page_ServiceRequest():
    return render_template("customer/SR-RETRO-001.html")