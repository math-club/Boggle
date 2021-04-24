# board.py

import random
from typing import Tuple

from .utils import chunked


class BoggleBoard:
    """Encapsulate a boggle board."""
    dices = (
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

    def __init__(self, size: int = 4):
        self.size = size
        self.content = self.generate()

    def generate(self) -> Tuple[Tuple[str]]:
        """Return a tuple of tuple contains random letters choosed in
        BoggleBoard.letters.
        """
        dices_result = tuple(random.choice(dices)
                             for dices in self.dices)

        return tuple(chunked(dices_result, self.size))

    @property
    def letters(self) -> str:
        """Return a string contains all letters which composed a boggle
        board in lower case.
        """
        letters = "".join("".join(letters)
                          for letters in self.content)

        return letters.lower()
