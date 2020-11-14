#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from flask import g

from films_repository import get_films_to_compare, save_comparison

app = Flask(__name__)


# Close handler
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def vs():
    films = get_films_to_compare()
    return render_template('vs.html', films=films)


@app.route('/rating')
def rating():
    return render_template('rating.html')


@app.route('/comparisons', methods=['POST'])
def add_comparison():
    win_id = int(request.form.get('win'))
    lose_id = int(request.form.get('lose'))
    save_comparison(win_id, lose_id)
    return redirect(url_for('vs'))


if __name__ == '__main__':
    app.run()
