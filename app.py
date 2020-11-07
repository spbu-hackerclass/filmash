#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import g

app = Flask(__name__)


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
