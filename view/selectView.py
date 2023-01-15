from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def all_emp():
    """List the names of all employees of the company"""
    connect = get_db_connection()
    data=connect.execute("""
    select full_name
    from employee
    
    """).fetchall()
    connect.close()
    th={'employee_name':'employee_names'}
    return render_template('select_all_emp.html', data=data, th=th)
def today():
    connect = get_db_connection()
    data = connect.execute("""
     select ID
     from invoice
     where _date >=Datetime('now','-1 day')
     """).fetchall()
    connect.close()
    return render_template('select_today_invoice.html', data=data)