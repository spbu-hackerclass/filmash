from typing import List, Tuple

from Film import Film
from db import query_db


def get_films_to_compare() -> Tuple[Film, Film]:
    films: List[Film] = query_db('SELECT * FROM films WHERE id IN (SELECT id FROM films ORDER BY RANDOM() LIMIT 2)')
    return films[0], films[1]
