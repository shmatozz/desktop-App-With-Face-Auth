"""
Application initializing file.
"""

import sys
from PyQt6.QtWidgets import QApplication
from windows.sign_in_window import SignIn   # sign in window
from windows.main_window import MainWindow  # main window
from user_data.data import *                # logged user data


def main():
    """ Main function.

    Init application window.

    If user was already logged -> init main menu window,

    else -> init sing in window

    :return: Zero on successful program and app finishing
    """
    app = QApplication(sys.argv)  # init app

    # if logged flag -> pass logged user to main menu
    if logged and len(login) > 0:
        main_menu = MainWindow(login)
        main_menu.show()
    # if no logged flag -> open sign in window
    else:
        sign_in_menu = SignIn()
        sign_in_menu.show()

    app.exec()  # close app


if __name__ == "__main__":
    main()
