from typing import TypedDict


class Film(TypedDict):
    id: int
    filmname: str
    filmdesc: str
    posterfile: str
    win: int
    lose: int
    rating: float
