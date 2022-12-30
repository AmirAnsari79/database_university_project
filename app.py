from flask import Flask, render_template
from models import Model, get_db_connection
import create_model_views as create_table_views
from view import customreView, carrierView, managerView, employeeView, package_managerView, operator_view

app = Flask(__name__)
app.secret_key = 'abc'


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# create database
app.add_url_rule('/createdb', view_func=create_table_views.create_db)
# create tables
app.add_url_rule('/createtables', view_func=create_table_views.create_table)
# customer viwe
app.add_url_rule('/customer', methods=['POST', 'GET'], view_func=customreView.customer_view)
app.add_url_rule('/insert_customer/', methods=['POST', 'GET'], view_func=customreView.get_insert_customer)
# employee view
app.add_url_rule('/employee', view_func=employeeView.employee_view)
app.add_url_rule('/insert_employee', methods=['POST', 'GET'], view_func=employeeView.get_insert_employee)
# carrier view
app.add_url_rule('/carrier', view_func=carrierView.carrier_view)
app.add_url_rule('/insert_carrier', methods=['POST', 'GET'], view_func=carrierView.get_insert_carrier)
# manager view
app.add_url_rule('/manager', view_func=managerView.manager_view)
app.add_url_rule('/insert_manager', methods=['POST', 'GET'], view_func=managerView.get_insert_manager)
# package_manager_view
app.add_url_rule('/package_manager', view_func=package_managerView.package_manager_view)
app.add_url_rule('/insert_package_manager', methods=['POST', 'GET'],
                 view_func=package_managerView.insert_packager_manager)

# operator view

app.add_url_rule('/operator', view_func=operator_view.operator_view)
app.add_url_rule('/insert_operator', methods=['POST', 'GET'], view_func=operator_view.insert_operator)

if __name__ == '__main__':
    app.run()
