from flask import Flask, render_template
from models import Model, get_db_connection
import create_model_views as create_table_views
from view import customreView, carrierView, managerView, employeeView, package_managerView, operator_view, serviceView, \
    invoiceView,selectView

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
app.add_url_rule('/Icarrier', view_func=carrierView.insert_carrier_view)
app.add_url_rule('/carrier', view_func=carrierView.delete_carrier_view)
app.add_url_rule('/Ucarrier', view_func=carrierView.update_carrier_view)
app.add_url_rule('/delete_carrier', methods=['POST', 'GET'], view_func=carrierView.delete_carrier)
app.add_url_rule('/insert_carrier', methods=['POST', 'GET'], view_func=carrierView.insert_carrier)
app.add_url_rule('/update_carrier', methods=['POST', 'GET'], view_func=carrierView.update_carrier)
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

# service view
app.add_url_rule('/service', view_func=serviceView.service_view)
app.add_url_rule('/insert_service', view_func=serviceView.insert_service, methods=['POST', 'GET'])
# invoice
app.add_url_rule('/invoice', view_func=invoiceView.invoice_view)
app.add_url_rule('/insert_invoice', view_func=invoiceView.insert_invoice, methods=['POST', 'GET'])


#select
app.add_url_rule('/select_all_emp',view_func=selectView.all_emp)
app.add_url_rule('/select_today_invoice',view_func=selectView.today)


if __name__ == '__main__':
    app.run()
