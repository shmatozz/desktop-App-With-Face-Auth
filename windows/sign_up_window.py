"""
File that implements all methods for Sign Up window correct working.
"""

import psycopg2                                       # PostgreSQL working lib
from PyQt6.QtWidgets import QMainWindow, QFileDialog  # PyQt classes for inheritance
from ui.sign_up import UiSignUp                       # sign up ui
from windows import connect_to_db
from windows.styles import *                          # window styles and resources
from facenet_pytorch import MTCNN                     # network for face detection
from PIL import Image                                 # image class for networks
from shutil import copy                               # function for copying photos


class SignUp(QMainWindow):
    """
    Backend of Sign Up window.

    This class implements methods for Sign Up window working.
    """
    def __init__(self, sign_in):
        """
        Initializing of Sign Up window.

        This method initialize user interface and connect buttons with methods.
        """
        super(SignUp, self).__init__()  # init QMainWindow class
        self.ui = UiSignUp()            # init sign up ui
        self.ui.setupUi(self)           # setup sign up ui
        self.sign_in = sign_in          # init sign in window to return
        self.face_auth = False          # face auth flag
        self.setWindowTitle("Sign Up")

        # connect buttons with methods
        self.ui.back_button.clicked.connect(self.back)       # back to sign in button
        self.ui.signup_button.clicked.connect(self.sign_up)  # sign up button
        self.ui.upload_button.clicked.connect(self.upload)   # upload photo button

    # sign up button pressed
    def sign_up(self):
        """
        Method for processing mouse click on "Sign Up" button in user interface.

        This method get user data from input fields and create new user in database of users.

        If some fields are missed -> mark them with red.
        """
        # cleaning styles
        self.reset_styles()

        # get fields text
        name = self.ui.name.text()                 # name
        surname = f"\'{self.ui.surname.text()}\'" if self.ui.surname.text() != '' else 'null'  # set 'null'
        email = f"\'{self.ui.email.text()}\'" if self.ui.email.text() != '' else 'null'        # if field is empty
        login = self.ui.login.text()               # login
        password = self.ui.password.text()         # password
        rep_password = self.ui.passwordRep.text()  # repeat password

        # if required fields are NOT missed -> try to create user account
        if len(name) > 0 and len(login) > 0 and len(password) > 0 and len(rep_password) > 0:
            # if passwords are not equal -> highlight password fields
            if password != rep_password:
                self.ui.RegistrationTitle.setText(NOT_EQUAL_PASSWORDS)                     # inform user
                self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))     # mark password field
                self.ui.passwordRep.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))  # mark repeat password field
            # if passwords ok -> try to connect to user database
            else:
                try:
                    connection = connect_to_db()    # establish connection
                    with connection.cursor() as cursor:  # init cursor to execute PostgreSQL command
                        # execute PostgreSQL command (select login)
                        cursor.execute(f"select login from users where login = '{login}'")
                        user_login = cursor.fetchone()   # receive query result
                        # if entered login already in database -> output info and highlight login field
                        if user_login is not None:
                            self.ui.RegistrationTitle.setText(OCCUPIED_LOGIN)                    # inform user
                            self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))  # mark login field
                        # if everything is OK -> add new user to owr database
                        else:
                            # if face auth flag = True -> add new user with face photo
                            if self.face_auth:
                                # execute PostgreSQL command (insert user info)
                                cursor.execute(f"insert into users (user_name, surname, email, login, password, "
                                               f"enable_face_auth, user_face) "
                                               f"values ('{name}', {surname}, {email}, '{login}', '{password}', "
                                               f"{self.face_auth}, "
                                               f"{psycopg2.Binary(open('user_data/face_photo.png', 'rb').read())})")
                            # if face auth flag = False -> add user without face photo
                            else:
                                # execute PostgreSQL command (insert user info)
                                cursor.execute(f"insert into users (user_name, surname, email, login, password) "
                                               f"values ('{name}', {surname}, {email}, '{login}', '{password}')")
                            connection.commit()  # save changes in database
                            self.back()          # return to sign in window

                        connection.close()       # close connection to database
                # processing database errors
                except psycopg2.Error:
                    print("[INFO] database work error")

        # if required fields are missed -> highlight missed fields
        else:
            self.ui.RegistrationTitle.setText(MISSING_REQUIRED_FIELDS)  # inform user
            for field in [self.ui.name, self.ui.login, self.ui.password, self.ui.passwordRep]:
                if len(field.text()) == 0:
                    field.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))  # mark field if length = 0

    # upload photo button pressed
    def upload(self):
        """
        Method for uploading image for creating user face pattern.

        If user upload face in registration -> face authentication will be available instantly.
        """
        dialog = QFileDialog(self)                             # init select file dialog window
        dialog.setDirectory(r'C:')                             # set default directory
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)  # set file mod
        dialog.setNameFilter("Images (*.png *.jpg)")           # set filename filter (only .png, .jpg)
        dialog.setViewMode(QFileDialog.ViewMode.List)          # set view mode
        # if dialog window closed -> process selected photo
        if dialog.exec():
            filename = dialog.selectedFiles()                  # get path of selected file
            # if any file was selected -> try to detect face
            if filename:
                mtcnn = MTCNN(image_size=160, margin=0, min_face_size=10)  # initializing mtcnn for face detection
                img = Image.open(filename[0])                  # open selected photo
                face, prob = mtcnn(img, return_prob=True, save_path="user_data/face_photo.png")
                # if no face detected or confidence of network < 95% -> inform user of incorrect photo
                if face is None or prob < 0.95:
                    self.ui.upload_mes.setText(INCORRECT_PHOTO)  # inform user
                # if face detected -> copy selected photo to user data
                else:
                    self.ui.upload_mes.setText(OK_PHOTO)        # inform user
                    self.face_auth = True                      # set face auth flag = True
                    copy(filename[0], "user_data/face_photo.png")  # copy photo to user data

    # back to sign in button pressed
    def back(self):
        """
        Returns back to Sign In window.
        """
        self.close()         # close sign up window
        self.sign_in.show()  # show sign in window

    # reset styles method
    def reset_styles(self):
        """
        Reset input lines styles. This method called to recolor fields after error output.
        """
        self.ui.name.setStyleSheet(DEFAULT_LINE_STYLE)         # reset name field
        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE)        # reset login field
        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE)     # reset password field
        self.ui.passwordRep.setStyleSheet(DEFAULT_LINE_STYLE)  # reset repeat password field
