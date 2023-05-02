import sys
from PyQt6.QtWidgets import QApplication
from windows.sign_in_window import SignIn
from windows.main_window import MainWindow
from user_data.data import *


def main():
    app = QApplication(sys.argv)

    if logged and len(login) > 0:
        main_menu = MainWindow(login)
        main_menu.show()
    else:
        sign_in_menu = SignIn()
        sign_in_menu.show()

    app.exec()


if __name__ == "__main__":
    main()
