# /source/movie.py
from typing import Iterator, Literal, TypeAlias

MovieData: TypeAlias = str | list[str]
Movie: TypeAlias = dict[Literal["title", "genre", "showtime"], MovieData]
DB: TypeAlias = dict[str, Movie]

db: DB = {
    "Kung Fu Panda": {
        "title": "Kung Fu Panda",
        "genre": "???",
        "showtime": ["1:00 PM", "5:00 PM"],
    },
    "Kung Fu Panda 2": {
        "title": "Kung Fu Panda",
        "genre": "???",
        "showtime": ["2:00 PM", "6:00 PM"],
    },
}


def add_movie(title: str, genre: str, showtime: list[str]) -> None:
    db[title] = {"title": title, "genre": genre, "showtime": showtime}


def find_movies_by_genre(genre: str) -> Iterator[Movie]:
    return (movie for movie in db.values() if movie["genre"] == genre)


def find_earliest_and_latest_showtime(title: str) -> tuple[str, str]:
    if (movie := db.get(title)) is None:
        raise KeyError

    return (movie["showtime"][0], movie["showtime"][-1])
