import psycopg2
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from ui.signUpMenu import UiSignUp
from windows.styles import *


class SignUp(QMainWindow):
    def __init__(self, sign_in):
        super(SignUp, self).__init__()
        self.ui = UiSignUp()
        self.ui.setupUi(self)
        self.sign_in = sign_in

        self.ui.backButton.clicked.connect(self.back)
        self.ui.SingUpButton.clicked.connect(self.sign_up)
        self.ui.uploadButton.clicked.connect(self.upload)

    def sign_up(self):
        # cleaning styles
        self.reset_styles()

        # get fields text
        name = self.ui.name.text()
        surname = self.ui.surname.text()
        email = self.ui.email.text()
        login = self.ui.login.text()
        password = self.ui.password.text()
        rep_password = self.ui.passwordRep.text()

        # if required fields are NOT missed
        if len(name) > 0 and len(login) > 0 and len(password) > 0 and len(rep_password) > 0:
            if password != rep_password:
                pass
        # if required fields are missed -> highlight missed fields
        else:
            self.ui.RegistrationTitle.setText("Required field are missed!")
            for field in [self.ui.name, self.ui.login, self.ui.password, self.ui.passwordRep]:
                if len(field.text()) == 0:
                    field.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))

    def upload(self):
        pass

    def back(self):
        self.close()
        self.sign_in.show()

    def reset_styles(self):
        self.ui.name.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.passwordRep.setStyleSheet(DEFAULT_LINE_STYLE)
