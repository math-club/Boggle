# main.py

from src.board import BoggleBoard
from src.utils import combinaisons
from src.word import Word


board = BoggleBoard()
print(board.letters)

word = input("Enter a word:").lower()
dictionary = Word.get_list()

print("Word is in board:", Word.is_in_board(word, board))
print("Word is in scrabble dictionary:", word.upper() in dictionary)
print("Word point:", Word.point(word))

<<<<<<< HEAD
<<<<<<< HEAD
    @classmethod
    def generate(cls) -> Tuple[Tuple[str]]:
        """Return a tuple of tuple contains random letters choosed in
        Grid.letters.
        """
        dices_result = tuple(random.choice(dices)
                             for dices in cls.dices)

        return tuple(chunked(dices_result, 4))


class Word:
    """Encapsulate a word."""
    scrabble_words_path = "data/scrabble.txt"

    @staticmethod
    def point_count(word: str) -> int:
        """Returns an int representing the point value of the given word."""
        word_length = len(word)

        points = letters_point.get(word_length)
        if points:
            return points
        else:
            return 0 if word_length < 3 else 11

    @classmethod
    def get_list(cls) -> Set[str]:
        """Returns a set containing all words allowed in scrabble with a
        length of more than 3 letters .
        """
        words_list =  open(Conf.scrabble_words_path,
                        encoding="utf-8")
        words = (word
                for line in iter(words_list)
                    if len(word := line.strip()) >= 3)

        return set(words)


def pretty_printer(grid: Grid) -> NoReturn:
    print("\n".join(" ".join(line)
                    for line in grid))


def combinaisons(letters: Sized) -> Tuple[str]:
    combinaisons = list()
    for i in range(3, len(letters) + 1):
        for comb in itertools.permutations(letters, i):
            combinaisons.append("".join(comb))

    return tuple(combinaisons)


<<<<<<< HEAD
def pretty_printer(grid: Grid) -> NoReturn:
    print("\n".join(" ".join(line)
                    for line in grid))
<<<<<<< HEAD

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
        coords_list: tuple = tuple((pos_letter_1[0] + move[0],
                            pos_letter_1[1] + move[1]) 
                            for move in moves)
        return tuple(coords for coords in coords_list 
            if (is_in_grid(grid, coords)
            AND (grid[coords[0]][coords[1]] == letter_2))

    for letter in word:
        letters_pos[letter]: list = []

    for line_nb, line in enumerate(grid):
        for letter_nb, letter in enumerate(line):
            if letter == word[0]:
                letters_pos[letter] += [(line_nb, letter_nb)]
<<<<<<< HEAD
    #TODO
    ...
=======

    for first_letter_pos in letters_pos[word[0]]:
        gen_word: str = ""
        letter_pos: tuple = first_letter_pos
        letter_index: int = 1
        for letter in word:
            for pos in proximity_search(letter_pos, word[letter_index]):
                gen_word += grid[pos[0]][pos[1]]
            #TODO
            letter_index += 1
        ...




#pretty_printer(grid())

#print(list(get_words()))
>>>>>>> a60ceec (Continue implementing word_tester)
=======
>>>>>>> 7d19cff (Fix type hinting.)
=======
print(combinaisons("hello"))
>>>>>>> 4af0b4d (Reformat code structure.)
=======
print("Words possibles:")
for comb in combinaisons(word):
    if comb in words_list:
        print(comb)
>>>>>>> b2d21a0 (Finish code reformat, rename main.py to boggle.py.)
=======
print("Words possibilities:")
for word in Word.combinaisons(board.letters):
    if word in dictionary:
        print(word)
>>>>>>> 8257574 (Improve API.)
