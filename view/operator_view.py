from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def operator_view():
    return render_template('insert_operator.html')


def insert_operator():
    if request.method == 'POST':
        operator_id = request.form['opid']
        h_work = request.form['hour_work']
        password = request.form['pass']
        try:
            connect = get_db_connection()
            connect.execute("""INSERT INTO operator (hour_work,pass,operator_id) VALUES (?,?,?)""",
                            (h_work, password, operator_id))
            connect.commit()
            connect.close()
            msg = "operator Reccord s"
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'{e}'
            return render_template('res.html', msg=msg)
    redirect(url_for('operator_view'))

