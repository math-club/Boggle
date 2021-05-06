# ui.py

import time

from src.board import BoggleBoard
from src.utils import combinaisons, pretty_print
from src.score import ScoreManager
from src.word import Word


class Timer:
    """Encapsulate a chronometer."""
    nb_seconds = 3*60  # 3 minutes.

    def __enter__(self) -> "Timer":
        """Start timer and return self."""
        self.start = time.time()
        return self

    def __exit__(self, *_):
        pass

    def time_elapsed(self):
        """Return the current timer
        """
        return time.time() - self.start

    def is_finished(self) -> bool:
        """Return true if timer is finished. False otherwise.
        If force is True, then the timer end automaticaly.
        """
        return self.time_elapsed() > self.nb_seconds


class Interface:
    """Encapsulate an user interface."""

    def __init__(self):
        self.board = BoggleBoard()
        self.dictionary = Word.get_list()

    def show_grid(self):
        print("Grille de Boggle :")
        print(pretty_print(self.board.letters))

    def is_valid(self, word: str) -> bool:
        return (Word.is_in_board(word, self.board)
                and word in self.dictionary)

    def get_user_input(self) -> str:
        """Return word typed by user."""
        print("Entrez un mot :")

        return input("  ").lower()

    def let_user_answered(self):
        """Let user answered until timer is not finished."""
        score = 0
        finden_words = []
        print("Chronomètre de 3 minutes lancé !")

        with Timer() as t:
            while not t.is_finished():
                word = self.get_user_input()

                try:
                    int(word.replace(" ", ""))
                    is_coord = True
                except ValueError:
                    is_coord = False

                if is_coord:
                    word = Word.positions_forms_word(word, self.board)
                if self.is_valid(word):
                    if word in finden_words:
                        print("Mot déjà trouvé !")
                    else:
                        print("Nouveau mot trouvé !")
                        finden_words.append(word)

                        word_point = Word.point(word)
                        print(f"  + {word_point} points ajoutés.")
                        score += word_point
                else:
                    print("  Ce mot ne peut pas être composé avec les lettres "
                        "de la grille ou n'est pas dans le dictionnaire du scrabble !")


        print("Le temps est écoulé !", end="\n"*2)

        print(f"Votre score est de {score}", end="\n"*2)

        print("Entrez votre nom pour enregistrer votre score :")
        name = input("  ")
        ScoreManager.register(name, score)

        print("Liste des meilleurs scores :")
        for name, value in ScoreManager.get_best():
            print(name, ": ", value)
        print()

        self.show_all_words()

        print("Merci d'avoir joué.")

    def show_all_words(self):
        print("Liste des mots possibles :")
        for word in Word.combinaisons(self.board.letters):
            if word in self.dictionary:
                print(" -", word)
