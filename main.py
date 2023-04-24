import sys
from PySide6.QtWidgets import QApplication
from windows.sign_in_window import SignIn
from windows.main_window import MainWindow
from data import *


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if logged and len(login) > 0:
        main_menu = MainWindow(login, password)
        main_menu.show()
    else:
        sign_in_menu = SignIn()
        sign_in_menu.show()

    app.exec()
