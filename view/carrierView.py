from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection

def carrier_view():
    return render_template('insert_carrier.html')


def get_insert_carrier():
    if request.method == 'POST':
        license_number = request.form['lnumber']
        PID = request.form['PID']
        try:
            connect = get_db_connection()
            connect.execute("""INSERT INTO carrier (license_number) VALUES (?)""", (license_number))
            connect.commit()
            connect.close()
            msg = 'carrier Record successfully added'
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'this error {e}'
            return render_template('res.html', msg=msg)
    return redirect('carrier_view')
