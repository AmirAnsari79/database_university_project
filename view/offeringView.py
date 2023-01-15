from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection


def offering_view():
    return render_template('insert_operator.html')


def insert_offering():
    if request.method == 'POST':
        CID = request.form['CID']
        POID = request.form['POID']
        SHID = request.form['SHID']
        try:
            connect = get_db_connection()
            connect.execute("""INSERT INTO offering (CID,POID,SHID) VALUES (?,?,?)""",
                            (CID, POID, SHID))
            connect.commit()
            connect.close()
            msg = "offering Record successfully inserted."
            return render_template('res.html', msg=msg)
        except Exception as e:
            msg = f'{e}'
            return render_template('res.html', msg=msg)


redirect(url_for('operator_view'))
