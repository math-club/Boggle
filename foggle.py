# boggle.py

from src.gui import Interface

def mainloop():
    while True:
        boggle = Interface()

        boggle.let_user_answered()

mainloop()