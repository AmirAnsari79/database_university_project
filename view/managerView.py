from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def manager_view():
    return render_template('insert_manager.html')


def get_insert_manager():
    if request.method == 'POST':
        locate = request.form['location']
        history = request.form['history']
        branch_id = request.form['branch_id']
        PMID = request.form['PMID']
        try:
            connect = get_db_connection()
            connect.execute("""INSERT INTO manager (location,hist_manage,branch_id) VALUES (?,?,?,?)""",
                            (locate, history, branch_id,PMID))
            connect.commit()
            connect.close()
            msg = 'manager Record successfully added'
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'{e}'
            return render_template('res.html', msg=msg)
    return redirect(url_for('manager_view'))
