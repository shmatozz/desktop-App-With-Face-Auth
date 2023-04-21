import sys
import psycopg2
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui.signInMenu import UiSignIn
from ui.signUpMenu import UiSignUp

DEFAULT_LINE_STYLE = "color: rgb(0, 0, 0);\n" \
                     "background-color: rgb(255, 255, 255);\n" \
                     "border-radius: 15px;\n" \
                     "border-radius: 15px; \n" \
                     "border: 2px solid #094065;\n" \
                     "padding-left: 20px\n"
DEFAULT_TITLE_STYLE = "color: rgb(0, 0, 0);"


class SingIn(QMainWindow):
    def __init__(self):
        super(SingIn, self).__init__()
        self.ui = UiSignIn()
        self.ui.setupUi(self)

        self.ui.SignInButton.clicked.connect(self.signIn)
        self.ui.SignUpButton.clicked.connect(self.openSignUp)

    def signIn(self):
        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.helloTitle.setStyleSheet(DEFAULT_TITLE_STYLE)

        # get logon and password from input text fields
        login = self.ui.login.text()
        password = self.ui.password.text()

        # empty fields check, if true -> mark red empty fields
        if len(login) == 0:
            self.ui.helloTitle.setText("Some fields are missed!")
            self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace("#094065", "#ff0200"))
        if len(password) == 0:
            self.ui.helloTitle.setText("Some fields are missed!")
            self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace("#094065", "#ff0200"))

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
                    self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace("#094065", "#ff0200"))
                # if database password == input password
                elif user_password[0] == password:
                    self.ui.helloTitle.setText("PASSED!")
                    self.ui.helloTitle.setStyleSheet("color: rgb(120, 183, 140);")

                    # TODO implement opening app main window
                # if database password != input password
                else:
                    self.ui.helloTitle.setText("Wrong password!")
                    self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace("#094065", "#ff0200"))

            connection.close()
        except psycopg2.Error as _ex:
            print("[INFO] Working error!")

    def openSignUp(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    sign_in = SingIn()
    sign_in.show()

    sys.exit(app.exec())
