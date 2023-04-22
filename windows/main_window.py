import psycopg2
from PySide6 import QtCore
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from ui.mainActivity import UiMainWindow
from windows.sign_up_window import SignUp
from windows.styles import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.animation = None
        self.ui = UiMainWindow()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.open_menu)

    def open_menu(self):
        width = self.ui.slide_menu_cont.width()
        if width == 0:
            new_width = 200
        else:
            new_width = 0

        self.animation = QPropertyAnimation(self.ui.slide_menu_cont)
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.start()
