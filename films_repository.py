from typing import List, Tuple

from Film import Film
from db import query_db, write_db, get_db


def get_films_to_compare() -> Tuple[Film, Film]:
    films: List[Film] = query_db('SELECT * FROM films WHERE id IN (SELECT id FROM films ORDER BY RANDOM() LIMIT 2)')
    return films[0], films[1]


def save_comparison(win_id: int, lose_id: int):
    win_film: Film = get_film(win_id)
    update_film_rating(win_id, win_film['win'] + 1, win_film['lose'])

    lose_film: Film = get_film(lose_id)
    update_film_rating(lose_id, lose_film['win'], lose_film['lose'] + 1)

    get_db().commit()


def get_film(id: int) -> Film:
    return query_db('SELECT * FROM films where id = ?', [id], True)


def update_film_rating(id: int, win: int, lose: int):
    write_db('UPDATE films SET win = ?, lose = ?, rating = ? WHERE id = ?', [win, lose, win / (win + lose), id])


def get_rating(n: int = 100) -> List[Film]:
    return query_db('SELECT * FROM films  ORDER BY rating DESC LIMIT ?', [n])
