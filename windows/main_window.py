import psycopg2
from PyQt6 import QtGui
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QDialog
from ui.confirm_dialog import UiConfirm
from ui.mainActivity import UiMainWindow
from ui.profile import UiProfile
from windows.styles import *


class Dialog(QDialog):
    def __init__(self, ok, cancel):
        super(Dialog, self).__init__()
        self.ui = UiConfirm()
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(ok)
        self.ui.cancel_button.clicked.connect(cancel)


class MainWindow(QMainWindow):
    def __init__(self, login, password):
        super(MainWindow, self).__init__()
        self.ui = UiMainWindow()  # main window ui
        self.ui.setupUi(self)
        self.profile = UiProfile()  # profile ui

        self.ui.button.clicked.connect(self.open_menu)
        self.ui.profile.clicked.connect(self.open_profile)

        self.login = login
        self.password = password
        self.animation = None
        self.dialog = None

    def open_menu(self):
        width = self.ui.slide_menu_cont.width()
        if width == 0:
            new_width = 200
            self.ui.button.setIcon(QtGui.QIcon(":/icons/icons/arrow_left.png"))
        else:
            new_width = 0
            self.ui.button.setIcon(QtGui.QIcon(":/icons/icons/menu.png"))

        self.animation = QPropertyAnimation(self.ui.slide_menu_cont, b"minimumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.start()

    # Profile ======================================
    # open user profile menu
    def open_profile(self):
        # change ui
        self.ui = self.profile
        self.ui.setupUi(self)

        try:
            # connect to database
            connection = self.connect_to_db()

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * from users where login = '{self.login}'")
                user_data = cursor.fetchone()  # returns tuple (uid, name, surname, email, login, password)

                self.ui.name_line.setText(user_data[1])  # set name
                self.ui.surname_line.setText(user_data[2])  # set surname
                self.ui.email_line.setText(user_data[3])  # set email
                self.ui.login_line.setText(user_data[4])  # set login

            connection.close()
        except psycopg2.Error as _ex:
            print("[INFO] database working error")

        # connect buttons of new ui
        self.ui.chanhe_password.clicked.connect(self.change_password)
        self.ui.save_button.clicked.connect(self.save_data)
        self.ui.back.clicked.connect(self.back_to_main)
        self.ui.exit_button.clicked.connect(self.exit_from_account)
        self.ui.vis_button.clicked.connect(self.toggle_password_visibility)
        # TODO realize photo upload by icon click

    # opens field for entering new password
    def change_password(self):
        self.profile.change_frame.setMinimumHeight(0)
        self.profile.change_frame.setMaximumHeight(0)
        self.profile.password_frame.setMaximumHeight(111)
        self.profile.password2_frame.setMaximumHeight(111)

    # show/hide password
    def toggle_password_visibility(self):
        if self.profile.password_line.echoMode() == QLineEdit.EchoMode.Password:
            self.profile.password_line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.profile.password2_line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.profile.vis_button.setIcon(QtGui.QIcon(":/icons/icons/view.png"))
        else:
            self.profile.password_line.setEchoMode(QLineEdit.EchoMode.Password)
            self.profile.password2_line.setEchoMode(QLineEdit.EchoMode.Password)
            self.profile.vis_button.setIcon(QtGui.QIcon(":/icons/icons/view_off.png"))

    # saving data to users database
    def save_data(self):
        name = self.profile.name_line.text()
        surname = self.profile.surname_line.text()
        email = self.profile.email_line.text()
        login = self.profile.login_line.text()
        new_password = self.profile.password_line.text()
        new_password = new_password if len(new_password) > 0 else self.password

        # if OK pressed in dialog window -> save info to users database
        def ok_pressed():
            try:
                # connect to database
                connection = self.connect_to_db()

                with connection.cursor() as cursor:
                    cursor.execute(f"select login from users where login = '{login}'")
                    info = cursor.fetchone()
                    if info is not None and info[0] != self.login:
                        self.profile.login_line.setText("Login is occupied!")
                        self.profile.login_line.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
                    else:
                        self.profile.login_line.setStyleSheet(DEFAULT_LINE_STYLE)
                        cursor.execute(f"update users "
                                       f"set user_name = '{name.capitalize()}', "
                                       f"surname = '{surname.capitalize()}', "
                                       f"email = '{email}', "
                                       f"login = '{login}', "
                                       f"password = '{new_password}' "
                                       f"where login = '{self.login}'")
                        connection.commit()

                        self.login = login
                        if new_password != self.password:
                            self.password = new_password

                # close connection
                connection.close()
            except psycopg2.Error as _ex:
                print("[INFO] database working error")

            self.dialog.close()

        # if CANCEL pressed in dialog window -> close window
        def cancel_pressed():
            self.dialog.close()

        # open dialog window
        self.dialog = Dialog(ok_pressed, cancel_pressed)
        self.dialog.show()

    # returns back to main menu
    def back_to_main(self):
        # change ui
        self.ui = UiMainWindow()
        self.ui.setupUi(self)

        # connect buttons of new ui
        self.ui.button.clicked.connect(self.open_menu)
        self.ui.profile.clicked.connect(self.open_profile)

    # exit from account to sing in menu
    def exit_from_account(self):
        pass
        # TODO implementation of account exit

    # establish connection to database
    @staticmethod
    def connect_to_db():
        return psycopg2.connect(host="127.0.0.1",
                                user="postgres",
                                password="1234567890",
                                database="app_users")
