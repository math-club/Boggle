# word.py

from collections import Counter
from typing import Dict, Set, Tuple

from src.board import BoggleBoard
from src.utils import combinaisons


Coordinates = Tuple[int]


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
        if word == None:
            return False
        word_counter = Counter(word)
        board_letters_counter = Counter(board.letters)

        for char in word:
            # If a letter is present several times and fewer times in
            # boggle board.
            if not (word_counter[char] <= board_letters_counter[char]):
                return False

        return True

    def is_in_grid(coords: Coordinates, board: BoggleBoard) -> bool:
        """
        Return True if position in grid, False if not
        """
        if coords[0] < 0 or coords[1] < 0:
            return False
        try:
            board.content[coords[0]][coords[1]]
        except IndexError:
            return False

        return True

    def proximity(center_coords: Coordinates, board: BoggleBoard) -> (
        Tuple[Coordinates]):
        """Return a tuple containing all adjacent coordinates
        """
        MOVES = (
            (-1, -1), (-1, 0), (-1, +1),
            (0, -1), (0, +1),
            (+1, -1), (+1, 0), (+1, +1)
        )

        coords_list = tuple((center_coords[0] + move[0],
                                    center_coords[1] + move[1])
                                        for move in MOVES)
        return tuple(coords
                         for coords in coords_list
                             if (Word.is_in_grid(coords, board)))

    def positions_forms_word(raw_input: str, board: BoggleBoard) -> str:
        """Return True if given coordinates forms a valid word in Boggle,
        False else.
        raw_input exemple: "00 01 12 13 23"
        """
        
        str_coordinates = tuple(raw_input.strip().strip("\n").split(" "))
        for coord in str_coordinates:
            if len(coord) != 2:
                return None
        coordinates = tuple((int(coord[0]),
                                  int(coord[1]))
                                   for coord in str_coordinates)

        previous_coord = coordinates[0]
        word = board.content[previous_coord[0]][previous_coord[1]]
        for coord in coordinates[1:]:
            if not coord in Word.proximity(previous_coord, board):
                return None
            word += board.content[coord[0]][coord[1]]
            previous_coord = coord
        word = word.lower()
        if word in Word.get_list():
            return word
        else:
            return None

    @staticmethod
    def combinaisons(letters: str) -> Set[str]:
        """Return a tuple contains all words possibilites with given set
        of letters.
        """
        return set(comb for comb in combinaisons(letters))

