from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def invoice_view():
    return render_template('insert_invoice.html')


def insert_invoice():
    if request.method == 'POST':
        amount = request.form['amount']
        addr = request.form['addr']
        service_type = request.form['type']
        CID = request.form['CID']
        POID = request.form['POID']
        try:
            connect = get_db_connection()
            connect.execute(
                """INSERT INTO invoice (_date,amount,addr,service_type,CID,POID) VALUES (time('now'),?,?,?,?,?)""",
                (amount, addr, service_type, CID, POID))
            connect.commit()
            connect.close()
            msg = 'ssss'
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = e
            return render_template('res.html', msg=msg)
    return redirect(url_for('invoice_view'))
