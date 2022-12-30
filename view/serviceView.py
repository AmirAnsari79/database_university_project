from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def service_view():
    return render_template('insert_service.html')


def insert_service():
    if request.method == 'POST':
        service_type = request.form['type']
        try:
            pass
            connect = get_db_connection()
            connect.execute("""INSERT INTO service (service_type) VALUES (?)""", (service_type))
            connect.commit()
            connect.close()
            msg='servie su'
            return render_template('res.html',msg=msg)
        except Exception as e:
            msg=e
            return render_template('res.html',msg=msg)
    redirect(url_for('service_view'))
