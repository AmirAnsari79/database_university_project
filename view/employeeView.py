from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def employee_view():
    return render_template('insert_employee.html')


def get_insert_employee():
    if request.method == 'POST':
        full_name = request.form['name']
        phone_number = request.form['phone_number']
        salary = request.form['salary']
        try:
            connect = get_db_connection()
            connect.execute("""
            INSERT INTO employee (full_name,phone_number,salary)
            VALUES (?,?,?)""", (full_name, phone_number, salary))
            connect.commit()
            connect.close()
            msg = "Employee Record successfully added"
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'this error {e}'
            return render_template('res.html', msg=msg)
    return redirect(url_for('employee_view'))
