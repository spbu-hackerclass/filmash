#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

from flask import Flask, render_template
from flask import g

app = Flask(__name__)

# Work with SQLite
DATABASE = 'films.db'


# Connect to DB
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Close handler
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def vs():
    return render_template('vs.html')


if __name__ == '__main__':
    app.run()
