"""
File that implements all methods for Sign In window correct working.
"""

import psycopg2                             # PostgreSQL working lib
import cv2                                  # camera capture lib
from torch import dist                      # distance between two photo tensors
from PIL import Image                       # image class for networks
from PyQt6.QtWidgets import QMainWindow     # PyQt QMainWindow class for inheritance
from ui.sign_in import UiSignIn             # sign in ui
from windows.sign_up_window import SignUp   # sign up class
from windows.main_window import MainWindow  # main window class
from windows.styles import *                # window styles and resources
from facenet_pytorch import MTCNN, InceptionResnetV1  # networks for face auth


class SignIn(QMainWindow):
    """
    Backend of Sign In window.

    This class implements methods for Sign In window working.
    """
    def __init__(self):
        """
        Initializing of Sign In window.

        This method initialize user interface and connect buttons with methods.
        """
        super(SignIn, self).__init__()  # init QMainWindow class
        self.sign_up = None             # init sign up window for opening
        self.main = None                # init main window for opening
        self.ui = UiSignIn()            # init sign in ui (current window)
        self.ui.setupUi(self)           # setup sign in ui (current window)
        self.cam = cv2.VideoCapture(0)  # init cam for face auth
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
        self.setWindowTitle("Log In")

        # connect buttons with methods
        self.ui.signin_button.clicked.connect(self.sign_in)      # sign in account button
        self.ui.signup_button.clicked.connect(self.open_sign_up)  # open sign up window button

    # sign in account button pressed
    def sign_in(self):
        """
        Method for processing mouse click on "Sign In" button in user interface.

        This method get user data from input fields or camera (in case of face authentication) and execute
        database to check matches.

        If some fields are missed -> mark them with red.
        """
        # cleaning styles of input fields
        self.reset_styles()

        # get login and password from input text fields
        login = self.ui.login.text()
        password = self.ui.password.text()

        # empty fields check, if true -> mark red empty fields
        if len(login) == 0:
            self.ui.helloTitle.setText(MISSING_REQUIRED_FIELDS)                     # inform user
            self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))     # mark empty field

        # get information from database
        try:
            connection = self.connect_to_db()       # establish connection
            with connection.cursor() as cursor:     # init cursor to execute PostgreSQL command
                # execute PostgreSQL command (select user password, face auth flag, user face photo)
                cursor.execute(f"select password, enable_face_auth, user_face from users where login = '{login}'")
                # receive query result
                info = cursor.fetchone()    # info[0] = password, info[1] = True/False face auth, info[2] = binary photo
            connection.close()                      # close connection
        # processing database errors
        except psycopg2.Error:
            print("[INFO] database error")

        # if user with such login was not found -> inform user
        if info is None:
            self.ui.helloTitle.setText(WRONG_LOGIN)                              # inform user
            self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))  # mark login field
        # if all fields are filled -> compare user input and info from database
        elif len(login) != 0 and len(password) != 0:
            # if database password == input password -> remember current user data and open main window
            if info[0] == password:
                # if user press remember me flag -> remember user data
                if self.ui.remember_me_check.isChecked():
                    with open("user_data/data.py", "w") as datafile:  # write current data to data file
                        datafile.seek(0)
                        datafile.write(f"logged = True\nlogin = '{login}'\npassword = '{password}'\n")
                        datafile.truncate()

                self.open_main_window(login)
            # if database password != input password
            else:
                self.ui.helloTitle.setText(WRONG_PASSWORD)                              # inform user
                self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))  # mark password field
        # if only login field entered and face auth is enable -> start face auth
        elif len(login) != 0 and info[1]:
            self.ui.helloTitle.setText(PROCESSING_FACE_AUTH)
            count_success = self.face_authentication(info)
            # if at least 1 try was successful -> remember current user data and open main window
            if count_success > 2:
                # if user press remember me flag -> remember user data
                if self.ui.remember_me_check.isChecked():
                    with open("user_data/data.py", "w") as datafile:  # write current data to data file
                        datafile.seek(0)
                        datafile.write(f"logged = True\nlogin = '{login}'\npassword = '{info[0]}'\n")
                        datafile.truncate()
                self.cam.release()             # close camera
                self.open_main_window(login)
            # if no successful try -> inform user
            else:
                self.ui.helloTitle.setText(TRY_AGAIN_OR_PASSWORD)
        # if login filled but password missed -> inform user
        else:
            self.ui.helloTitle.setText(MISSING_REQUIRED_FIELDS)  # inform user
            self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))  # mark empty field

    def face_authentication(self, info):
        """
        Check user face with face patten from database.

        :param info: Array of user data received from database by entered login.
        :return: Count of successful trys in faces match.
        """
        with open("user_data/face_photo.png", "wb") as photo:  # binary write database photo to current user data
            photo.write(info[2])
        mtcnn = MTCNN(image_size=160, margin=0, min_face_size=10)        # init mtcnn for face detection
        resnet = InceptionResnetV1(pretrained='vggface2').eval()          # init resnet for face to embedding conversion
        face_database = mtcnn(Image.open("user_data/face_photo.png"))     # pass face from user database
        emb_database = resnet(face_database.unsqueeze(0)).detach()        # get embedding matrix
        count_trys = 0                                                    # init try count of face auth
        count_success = 0                                                 # init successful try count of face auth
        while count_trys < 5 and count_success < 3:
            result, image = self.cam.read()                               # get image from camera
            cv2.imwrite("user_data/face_photo.png", image)                # write image to user face
            face_current = mtcnn(Image.open("user_data/face_photo.png"))  # get cropped face of user
            # if face was detected on image -> calculate distance with database face
            if face_current is not None:
                emb_current = resnet(face_current.unsqueeze(0)).detach()  # get embedding matrix
                distance = dist(emb_current, emb_database).item()         # calculate distance
                print(distance)
                # if distance is rather small -> inc success count
                if distance < 0.5:
                    count_success += 1
            count_trys += 1

        return count_success

    # sign up button pressed
    def open_sign_up(self):
        """
        Open window for user registration.
        """
        self.close()                 # close sign in window
        self.sign_up = SignUp(self)  # init sign up window
        self.sign_up.show()          # show sign up window

    def open_main_window(self, login):
        """
        Open main window of application.
        """
        self.close()                   # close sign in window
        self.main = MainWindow(login)  # init main window
        self.main.show()               # open main window

    # reset styles method
    def reset_styles(self):
        """
        Reset input lines styles. This method called to recolor fields after error output.
        """
        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE)        # reset login styles
        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE)     # reset password styles
        self.ui.helloTitle.setStyleSheet(DEFAULT_TITLE_STYLE)  # reset title styles

    # establish database connection
    @staticmethod
    def connect_to_db():
        """
        Establish connection with users database.
        """
        return psycopg2.connect(host="db.dkadcfuknosrclhomisf.supabase.co",
                                user="postgres",
                                password="verifacetion123",
                                database="postgres")
