#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Tuple, Union

from flask import Flask, render_template
from flask import g

from Film import Film
from films_repository import get_films_to_compare

app = Flask(__name__)


# Close handler
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def vs():
    films: Tuple[Film, Film] = get_films_to_compare()

    return render_template('vs.html', films=films)


if __name__ == '__main__':
    app.run()
