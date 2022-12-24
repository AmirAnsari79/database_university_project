import sqlite3

from flask import Flask, render_template, request, flash
from models import Model, get_db_connection


def customer_view():
    return render_template('insert_customer.html')


def get_insert_customer():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone']
        if not name:
            flash('name is required!')
        elif not phone_number:
            flash('phone number is required!')
        else:
            connect = get_db_connection()
            connect.execute("""INSERT INTO customer (full_name,phone_number)
            VALUES(?, ?)""", (name, phone_number))

            connect.commit()
            connect.close()
            msg = "Record successfully added"
            return render_template("res.html",msg=msg)
        # return render_template('insert_customer.html')
