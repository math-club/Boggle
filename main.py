
import random
from typing import Iterable, NoReturn

from conf import Conf
from utils import chunked


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


def get_words() -> set[str]:
    """Returns a set containing all words allowed in scrabble with a length of
    more than 3 letters .
    """
    words_list =  open(Conf.scrabble_words_path,
                       encoding="utf-8")
    words = (word
             for line in iter(words_list)
                if len(word := line.strip()) >= 3)

    return set(words)


def point_count(word: str) -> int:
    """Returns an int representing the point value of the given word."""
    word_length = len(word)

    if (points := letters_point.get(word_length)):
        return points
    else:
        return 0 if word_length < 3 else 11


def grid() -> tuple[tuple[str]]:
    """Returns a tuple of four tuples containing the random result of a
    dice roll.
    """
    dices_result: tuple[str] = tuple(random.choice(dices)
                                     for dices in DICES)

    return tuple(chunked(dices_result, 4))


def pretty_printer(grid: tuple[tuple]) -> NoReturn:
    print("\n".join(" ".join(line)
                    for line in grid))

def is_in_grid(grid: tuple[tuple], coords: tuple[int]) -> bool:
    """
    Return True if position in grid, False if not
    """
    if coords[0] < 0 or coords[1] < 0:
        return False
    try:
        grid[coords[0]][coords[1]]
    except IndexError:
        return False
    return True

def word_tester(grid: tuple[tuple], dictio: dict, word: str) -> bool:
    """
    Return True if word in grid and dict, False if not
    """
    word: str = "" .join(letter.capitalize() for letter in word)

    if not(word in get_words()):
        return False

    moves: tuple[tuple[int]] = ((-1, -1), (-1, 0), (-1, +1)
                                (0, -1), (0, +1)
                                (+1, -1), (+1, 0), (+1, +1))
    letters_pos: dict = {}

    def proximity_search(pos_letter_1: tuple[int], letter_2: str) -> tuple:
        coords: list = []
        for move in moves:
            coords += [(pos_letter_1[0] + move[0],
                        pos_letter_1[1] + move[1])]
        #TODO
        ...

    for letter in word:
        letters_pos[letter]: list = []

    for line_nb, line in enumerate(grid):
        for letter_nb, letter in enumerate(line):
            if letter == word[0]:
                letters_pos[letter] += [(line_nb, letter_nb)]
    #TODO
    ...
