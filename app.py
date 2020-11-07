#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import g

from films_repository import get_films_to_compare

app = Flask(__name__)


# Close handler
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    films = get_films_to_compare()
    return render_template('vs.html')


if __name__ == '__main__':
    app.run()
