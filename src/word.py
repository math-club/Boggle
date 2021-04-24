# word.py

from collections import Counter
from typing import Dict, Set

from .board import BoggleBoard
from .utils import combinaisons


class Word:
    """Contains some variables and methods related to word."""
    dictionary_path = "data/scrabble.txt"

    word_point_value: Dict[int, int] = {
        3: 1,
        4: 1,
        5: 2,
        6: 3,
        7: 5,
        8: 11
    }

    @classmethod
    def point(cls, word: str) -> int:
        """Returns an int representing the point value of the given
        word.
        """
        word_length = len(word)
        word_point = cls.word_point_value.get(word_length)

        if word_point is None:
            return 0 if word_length < 3 else 11
        else:
            return word_point

    @classmethod
    def get_list(cls) -> Set[str]:
        """Returns a set containing all words allowed in scrabble with a
        length of more than 3 letters .
        """
        words_list = open(cls.dictionary_path,
                          encoding="utf-8")
        words = (word.lower()
                for line in iter(words_list)
                    if len(word := line.strip()) >= 3)

        return set(words)

    @staticmethod
    def is_in_board(word: str, board: BoggleBoard) -> bool:
        """Return true if given word can be composed with letters of
        given boggle board. False else.
        """
        word_counter = Counter(word)
        board_letters_counter = Counter(board.letters)

        for char in word:
            # If a letter is present several times and fewer times in
            # boggle board.
            if not (word_counter[char] <= board_letters_counter[char]):
                return False

        return True

    @staticmethod
    def combinaisons(letters: str) -> Set[str]:
        """Return a tuple contains all words possibilites with given set
        of letters.
        """
        return set(comb for comb in combinaisons(letters))

