import psycopg2
import cv2
from torch import dist
from PIL import Image
from PyQt6.QtWidgets import QMainWindow
from ui.signInMenu import UiSignIn
from windows.sign_up_window import SignUp
from windows.main_window import MainWindow
from windows.styles import *
from facenet_pytorch import MTCNN, InceptionResnetV1


class SignIn(QMainWindow):
    def __init__(self):
        super(SignIn, self).__init__()
        self.sign_up = None
        self.main = None
        self.ui = UiSignIn()
        self.ui.setupUi(self)
        self.cam = cv2.VideoCapture(0)

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
            self.ui.helloTitle.setText("Missing required fields!")
            self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
        if len(password) == 0:
            self.ui.helloTitle.setText("Missing required fields!")
            self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))

        try:
            connection = self.connect_to_db()
            with connection.cursor() as cursor:
                cursor.execute(f"select password, enable_face_auth, user_face from users where login = '{login}'")
                info = cursor.fetchone()    # info[0] = password, info[1] = True/False face auth, info[2] = binary photo
            connection.close()
        except psycopg2.Error:
            print("[INFO] database error")

        if len(login) != 0 and len(password) != 0:
            if info is None:
                self.ui.helloTitle.setText("Wrong login!")
                self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
            # if database password == input password
            elif info[0] == password:
                with open("user_data/data.py", "w") as datafile:
                    datafile.seek(0)
                    datafile.write(f"logged = True\nlogin = '{login}'\npassword = '{password}'\n")
                    datafile.truncate()

                self.ui.helloTitle.setText("PASSED!")
                self.ui.helloTitle.setStyleSheet("color: rgb(120, 183, 140);")
                self.close()
                self.main = MainWindow(login)
                self.main.show()
            # if database password != input password
            else:
                self.ui.helloTitle.setText("Wrong password!")
                self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
        elif len(login) != 0 and info[1]:
            with open("user_data/face_photo.png", "wb") as photo:
                photo.write(info[2])
            mtcnn = MTCNN(image_size=1000, margin=0, min_face_size=20)  # initializing mtcnn for face detection
            resnet = InceptionResnetV1(pretrained='vggface2').eval()
            face_database = mtcnn(Image.open("user_data/face_photo.png"))
            emb_database = resnet(face_database.unsqueeze(0)).detach()
            count_trys = 0
            count_success = 0
            while count_trys < 2:
                result, image = self.cam.read()
                cv2.imwrite("user_data/face_photo.png", image)
                face_current = mtcnn(Image.open("user_data/face_photo.png"))
                if face_current is not None:
                    emb_current = resnet(face_current.unsqueeze(0)).detach()
                    distance = dist(emb_current, emb_database).item()
                    print(distance)
                    if distance < 0.6:
                        count_success += 1
                count_trys += 1
            self.cam.stop()
            if count_success > 0:
                with open("user_data/data.py", "w") as datafile:
                    datafile.seek(0)
                    datafile.write(f"logged = True\nlogin = '{login}'\npassword = '{info[0]}'\n")
                    datafile.truncate()
                self.close()
                self.main = MainWindow(login)
                self.main.show()
            else:
                self.ui.helloTitle.setText("Error, try again or use your password")

    def openSignUp(self):
        self.close()
        self.sign_up = SignUp(self)
        self.sign_up.show()

    def reset_styles(self):
        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.helloTitle.setStyleSheet(DEFAULT_TITLE_STYLE)

    @staticmethod
    def connect_to_db():
        return psycopg2.connect(host="127.0.0.1",
                                user="postgres",
                                password="1234567890",
                                database="app_users")
