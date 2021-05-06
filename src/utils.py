# utils.py

import itertools

from typing import NoReturn, Iterable, Sequence, Tuple


def combinaisons(letters: str) -> Iterable[str]:
    """Yield word by word all possibles combinations of word composed
    with given letters of more 3 letters.
    """
    letters = "".join(letters)

    for i in range(3, len(letters) + 1):
        for comb in itertools.combinations(letters, i):
            yield "".join(comb)


def chunked(seq: Sequence, n: int) -> Iterable:
    """Returns an iterable that contains given iterable separated into n
    bundles.
    """
    return (seq[chunk:chunk + n]
            for chunk in range(0, len(seq), n))


def pretty_print(letters: str) -> NoReturn:
    """Returns printable string with given letter as grid form."""
    pretty_string = ""
    for line in chunked(letters, 4):
        pretty_string += " ".join(char for char in line)
        pretty_string += "\n"
    return pretty_string