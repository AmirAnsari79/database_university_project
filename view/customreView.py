from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def customer_view():
    return render_template('add_invoice.html')


def get_insert_customer():
    if request.method == 'POST':
        name = request.form['name']
        cid = request.form['cid']
        phone_number = request.form['phone']
        if not name:
            flash('name is required!')
        elif not phone_number and not phone_number.startswith('09') and len(phone_number) != 11:
            flash('phone number is required!')
        elif len(cid) != 10:
            flash('this cid is incorrect')
        else:
            try:
                connect = get_db_connection()
                connect.execute("""INSERT INTO customer (full_name,phone_number,cid)
                VALUES(?, ?, ?)""", (name, phone_number, cid))

                connect.commit()
                connect.close()

                msg = "Customer Record successfully added"
                return render_template("res.html", msg=msg)
            except Exception as e:
                msg = f'your error is {e}'
                return render_template("res.html", msg=msg)

    # return render_template('add_invoice.html')
    return redirect(url_for('customer_view'))
