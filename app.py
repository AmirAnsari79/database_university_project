from flask import Flask, render_template
from models import Model, get_db_connection

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/createdb')
def create_db():
    get_db_connection()
    return 'database is create'


@app.route('/create_table')
def create_table():
    Model.create_customer()
    Model.create_carrier()
    Model.create_employee()
    Model.create_invoice()
    Model.create_manager()
    Model.create_offering()
    Model.create_operator()
    Model.create_packagingManager()
    Model.create_service()
    Model.create_service_type()
    return 'crate_table'


@app.route('/insert_customer')
def insert_customer():
    if True:
        return render_template('insert_customer.html')





if __name__ == '__main__':
    app.run()
