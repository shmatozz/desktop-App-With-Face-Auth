import psycopg2
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from ui.signInMenu import UiSignIn
from ui.signUpMenu import UiSignUp
from windows.sign_up_window import SignUp
from windows.styles import *


class SignIn(QMainWindow):
    def __init__(self):
        super(SignIn, self).__init__()
        self.sign_up = None
        self.ui = UiSignIn()
        self.ui.setupUi(self)

        self.ui.SignInButton.clicked.connect(self.signIn)
        self.ui.SignUpButton.clicked.connect(self.openSignUp)

    def signIn(self):
        # cleaning styles
        self.reset_styles()

        # get logon and password from input text fields
        login = self.ui.login.text()
        password = self.ui.password.text()

        # empty fields check, if true -> mark red empty fields
        if len(login) == 0:
            self.ui.helloTitle.setText("Some fields are missed!")
            self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
        if len(password) == 0:
            self.ui.helloTitle.setText("Some fields are missed!")
            self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))

        if len(login) != 0 and len(password) != 0:
            try:
                # connect to database
                connection = psycopg2.connect(host="127.0.0.1",
                                              user="postgres",
                                              password="1234567890",
                                              database="app_users")

                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT password from users where login = '{login}'")
                    user_password = cursor.fetchone()

                    # if no user with such login
                    if user_password is None:
                        self.ui.helloTitle.setText("Wrong login!")
                        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
                    # if database password == input password
                    elif user_password[0] == password:
                        self.ui.helloTitle.setText("PASSED!")
                        self.ui.helloTitle.setStyleSheet("color: rgb(120, 183, 140);")

                        # TODO implement opening app main window
                    # if database password != input password
                    else:
                        self.ui.helloTitle.setText("Wrong password!")
                        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
                # close connection to database
                connection.close()
            except psycopg2.Error as _ex:
                print("[INFO] Working error!")

    def openSignUp(self):
        self.close()
        self.sign_up = SignUp(self)
        self.sign_up.show()

    def reset_styles(self):
        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.helloTitle.setStyleSheet(DEFAULT_TITLE_STYLE)
