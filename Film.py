from typing import TypedDict


class Film(TypedDict):
    id: int
    filmname: str
    posterfile: str
    win: int
    lose: int
    rating: float
