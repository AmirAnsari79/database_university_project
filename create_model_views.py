from flask import Flask, render_template
from models import Model, get_db_connection


def create_db():
    get_db_connection()
    return 'database is create'


def create_table():
    Model.create_customer()
    Model.create_carrier()
    Model.create_employee()
    Model.create_operator()
    Model.create_invoice()
    Model.create_manager()
    Model.create_offering()
    Model.create_packagingManager()
    Model.create_service()
    # Model.create_service_type()
    return 'crate_table'
