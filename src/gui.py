#gui.py

__author__ = "math-club"


import PySimpleGUI as sg

from src.ui import Timer
from src.board import BoggleBoard
from src.utils import combinaisons, pretty_print
from src.score import ScoreManager
from src.word import Word

sg.theme("DarkAmber")

LICENSE = "GNU GPL v3"
GAME_NAME = "Foggle"
GAME_DESC = ("Ce jeu est similaire au Boggle. Une grille de 4*4 lettres "
            "est générée à partir de dés, et vous devez y chercher de mots. "
            "Au {0}, la seule règle est de former des mots à partir "
            "des lettres présentent sur la grille. Le temps imparti est de "
            "3 minutes.\nSi vous souhaitez suivre les règles du Boggle, alors "
            "vous devrez entrer les coordonnées de chaque lettre sous la forme "
            "suivante: '00 01 11 22 21' où chaque couple de chiffres est formé "
            "de l'indice de la colonne, suivi de l'indice de la ligne, sachant "
            "que l'indexage commence à 0 (l'indice de la première ligne ou "
            "colonne est donc 0, celui dela dernière, 3).\nÀ la fin des 3 "
            "minutes, votre score est affiché, les mots longs valant plus de "
            "points, jusqu'à 8 lettres. Une liste des mots possibles selon les "
            "règles du {0} est également affichée").format(GAME_NAME)


class Interface:
    """Encapsulate an user interface."""

    def __init__(self):
        self.board = BoggleBoard()
        self.dictionary = Word.get_list()
        self.layout = [
            [sg.Text(GAME_NAME, font = ("", 32)),
            sg.Text("180s", font = ("", 32), key = "-TIMER-")],

            [sg.Text(self.get_grid_str(), font = ("", 16)),
            sg.VerticalSeparator(pad = (30, 5)),
            sg.Text("Chronomètre de 3 minutes lancé !", size = (50, 11), key = "-OUT-"),],

            [sg.Input("Trouve un mot", key = "-INPUT-"),
            sg.Button("OK", key = "-SEARCH-")],

            [sg.Button("Nouvelle Partie", key = "-RESTART-"),
            sg.Button("Current Words", key = "-SPOILER-"),
            sg.Button("Crédits", key = "-CREDITS-"),
            sg.Button("Règles", key = "-RULES-"),
            sg.Button("License", key = "-LICENSE-")]
        ]
        self.window = sg.Window("%s by %s" % (GAME_NAME, __author__), 
                                self.layout)

    def get_grid_str(self):
        grid = "Grille de Boggle:\n\n"
        return grid + pretty_print(self.board.letters)

    def is_valid(self, word: str) -> bool:
        return (Word.is_in_board(word, self.board)
                and word in self.dictionary)

    def let_user_answered(self):
        """Let user answered until timer is not finished."""
        score = 0
        finden_words = []
        is_forced = False

        with Timer() as t:
            while not t.is_finished():
                event, values = self.window.read()
                self.window["-TIMER-"]((str(180 - int(t.time_elapsed())) + "s"))

                if event == "-SEARCH-":
                    word = values["-INPUT-"]

                    try:
                        int(word.replace(" ", ""))
                        is_coord = True
                    except ValueError:
                        is_coord = False

                    if is_coord:
                        word = Word.positions_forms_word(word, self.board)
                    if self.is_valid(word):
                        if word in finden_words:
                            output = "Mot déjà trouvé !"
                        else:
                            output = "Nouveau mot trouvé !\n"
                            finden_words.append(word)

                            word_point = Word.point(word)
                            output += f"  + {word_point} points."
                            score += word_point
                    else:
                        output = ("Ce mot ne peut pas être composé avec les lettres\n "
                            "de la grille ou n'est pas dans le dictionnaire du scrabble !")

                    self.window["-OUT-"].update(output)
                if event == sg.WIN_CLOSED:
                    self.window.close()
                    quit()
                if event == "-RESTART-":
                    break
                if event == "-RULES-":
                    sg.popup(GAME_DESC, title = "Règles")
                if event == "-CREDITS-":
                    sg.popup("Crédits:\n\n%s by %s\nLicense: %s" % 
                        (GAME_NAME, __author__, LICENSE),title = ("Crédits"))
                if event == "-LICENSE-":
                    with open("LICENSE") as license_file:
                        sg.popup_scrolled("\n".join(license_file.readlines()),
                        title = "License")
                if event == "-SPOILER-":
                    sg.popup_scrolled(self.show_all_words(), title = "Current Words")


        output = "Le temps est écoulé !\n"
        output += f"Votre score est de {score}\n"
        output += "Entrez votre nom pour enregistrer votre score, 0 pour passer"
        self.window["-OUT-"].update(output)

        event, values = self.window.read()
        if event == "-SEARCH-":
            name = values["-INPUT-"]
            if name != "0":
                ScoreManager.register(name, score)

            output = "Merci d'avoir joué."
            output = ("Liste des meilleurs scores :\n")
            for name, value in ScoreManager.get_best():
                output +=  "%s: %s\n" % (name, value)
            self.window["-OUT-"].update(output)

        scroll_output = self.show_all_words()

        event, values = self.window.read()
        if event == "-RESTART-":
            pass

    def show_all_words(self):
        output = "Liste des mots possibles :\n"
        words = []
        for word in Word.combinaisons(self.board.letters):
            if word in self.dictionary:
                words.append(word)
        output += "- " + "\n- ".join(sorted(words))
        return output


