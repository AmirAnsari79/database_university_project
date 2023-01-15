from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def insert_carrier_view():
    return render_template('insert_carrier.html')


def update_carrier_view():
    return render_template('update_carrier.html')


def delete_carrier_view():
    return render_template('delete_carrier.html')


def insert_carrier():
    if request.method == 'POST':
        license_number = request.form['lnumber']
        PID = request.form['PID']
        try:
            connect = get_db_connection()
            connect.execute("""INSERT INTO carrier (license_number,PCID) VALUES (?,?)""", (license_number, PID))
            connect.commit()
            connect.close()
            msg = 'carrier Record successfully added'
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'this error {e}'
            return render_template('res.html', msg=msg)
    return redirect('insert_carrier_view')


def update_carrier():
    if request.method == 'POST':
        license_number = request.form['lnumber']
        PID = request.form['PID']
        try:
            connect = get_db_connection()
            connect.execute("""UPDATE carrier SET license_number =(?) WHERE PCID=(?);""", (license_number, PID))
            connect.commit()
            connect.close()
            msg = 'carrier Update successfully'
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'this error {e}'
            return render_template('res.html', msg=msg)
    return redirect('update_carrier_view')


def delete_carrier():
    if request.method == 'POST':
        PCID = request.form['PCID']
        try:
            connect = get_db_connection()
            connect.execute("""DELETE FROM carrier WHERE (PCID=?) """, (PCID))
            connect.commit()
            connect.close()
            msg = 'carrier Delete successfully'
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'this error {e}'
            return render_template('res.html', msg=msg)
    return redirect('delete_carrier_view')
