import sqlite3

from flask import Flask, render_template, request, flash, redirect, url_for
from models import Model, get_db_connection




def get_insert_invoice():
    if request.method == 'POST':
        pass




