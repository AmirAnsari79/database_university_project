from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def package_manager_view():
    return render_template('insert_package_manager.html')


def insert_packager_manager():
    if request.method == 'POST':
        pack_in_day = request.form['PIND']
        PAID = request.form['PAID']
        try:
            connect = get_db_connection()
            connect.execute("""INSERT INTO package_manager (package_in_daym,PAID) VALUES (?,?)""", (pack_in_day,PAID))
            connect.commit()
            connect.close()
            msg = "Package manager Record successfully added"
            return render_template('res.html',msg=msg)
        except Exception as e:
            msg=f'{e}'
            return render_template('res.html',msg=msg)
    return redirect(url_for('package_manager_view'))