
from itertools import islice
from typing import Iterable

from conf import Conf


DICES: tuple[tuple[str]] = (
    ("L", "E", "N", "U", "Y", "G"),
    ("E", "L", "U", "P", "S", "T"),
    ("Z", "D", "V", "N", "E", "A"),
    ("S", "D", "T", "N", "O", "E"),
    ("A", "M", "O", "R", "I", "S"),
    ("F", "X", "R", "A", "O", "I"),
    ("M", "O", "Q", "A", "B", "J"),
    ("F", "S", "H", "E", "E", "I"),
    ("H", "R", "S", "N", "E", "I"),
    ("E", "T", "N", "K", "O", "U"),
    ("T", "A", "R", "I", "L", "B"),
    ("T", "I", "E", "A", "O", "A"),
    ("A", "C", "E", "P", "D", "M"),
    ("R", "L", "A", "S", "E", "C"),
    ("U", "L", "I", "W", "E", "R"),
    ("V", "G", "T", "N", "I", "E")
)


def get_words() -> Iterable[str]:
    """Returns a generator containing all words allowed in scrabble."""
    words_list =  open(Conf.scrabble_words_path,
                       encoding="utf-8")
    words = (line.strip()
                 for line in iter(words_list))

    return islice(words, 1, None)


def point_count(word: str) -> int:
    """Returns an int representing the point value of the given word."""
    letters_point: dict[int, int] = {
        3: 1
        4: 1,
        5: 2,
        6: 3,
        7: 5,
        8: 11
    }
    word_length = len(word)

    if (points := letters_point.get(word_length):
        return points
    else:
        return 0 if word_length < 3 else 11
