

class Conf:
    scrabble_words_path = "data/scrabble.txt"

    letters_point: dict[int, int] = {
        3: 1,
        4: 1,
        5: 2,
        6: 3,
        7: 5,
        8: 11
    }
