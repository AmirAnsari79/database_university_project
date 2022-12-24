from flask import Flask, render_template
from models import Model, get_db_connection
import create_model_views as create_table_views
import insert_views

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.add_url_rule('/createdb', view_func=create_table_views.create_db)
app.add_url_rule('/createtables', view_func=create_table_views.create_table)
app.add_url_rule('/customerviews/',methods=['POST','GET'], view_func=insert_views.customer_view)
app.add_url_rule('/insertcustomer/',methods=['POST','GET'], view_func=insert_views.get_insert_customer)

if __name__ == '__main__':
    app.run()
