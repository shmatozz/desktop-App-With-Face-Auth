import psycopg2
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from ui.signUpMenu import UiSignUp
from windows.styles import *
from facenet_pytorch import MTCNN
from PIL import Image
from shutil import copy


class SignUp(QMainWindow):
    def __init__(self, sign_in):
        super(SignUp, self).__init__()
        self.ui = UiSignUp()
        self.ui.setupUi(self)
        self.sign_in = sign_in
        self.face_auth = False

        self.ui.backButton.clicked.connect(self.back)
        self.ui.SingUpButton.clicked.connect(self.sign_up)
        self.ui.uploadButton.clicked.connect(self.upload)

    def sign_up(self):
        # cleaning styles
        self.reset_styles()

        # get fields text
        name = self.ui.name.text()
        surname = f"\'{self.ui.surname.text()}\'" if self.ui.surname.text() != '' else 'null'  # set 'null'
        email = f"\'{self.ui.email.text()}\'" if self.ui.email.text() != '' else 'null'        # if field is empty
        login = self.ui.login.text()
        password = self.ui.password.text()
        rep_password = self.ui.passwordRep.text()

        # if required fields are NOT missed
        if len(name) > 0 and len(login) > 0 and len(password) > 0 and len(rep_password) > 0:
            # if passwords are not equal -> highlight password fields
            if password != rep_password:
                self.ui.RegistrationTitle.setText("Passwords are not equal")
                self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
                self.ui.passwordRep.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
            # if passwords ok -> try to connect to user database
            else:
                try:
                    # establish connection
                    connection = self.connect_to_db()

                    with connection.cursor() as cursor:
                        # checking login existence
                        cursor.execute(f"select login from users where login = '{login}'")
                        user_login = cursor.fetchone()
                        # if entered login already in database -> output info and highlight login field
                        if user_login is not None:
                            self.ui.RegistrationTitle.setText("Login is already occupied")
                            self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
                        # if everything is OK -> add new user to owr database
                        else:
                            if self.face_auth:
                                cursor.execute(f"insert into users (user_name, surname, email, login, password, "
                                               f"enable_face_auth, user_face) "
                                               f"values ('{name}', {surname}, {email}, '{login}', '{password}', "
                                               f"{self.face_auth}, "
                                               f"{psycopg2.Binary(open('user_data/face_photo.png', 'rb').read())})")
                            else:
                                cursor.execute(f"insert into users (user_name, surname, email, login, password) "
                                               f"values ('{name}', {surname}, {email}, '{login}', '{password}')")
                            connection.commit()

                            # if no error -> returns back to sign in window
                            self.back()

                        # close connection to database
                        connection.close()
                except psycopg2.Error as er:
                    print(er)
                    print("[INFO] database work error")

        # if required fields are missed -> highlight missed fields
        else:
            self.ui.RegistrationTitle.setText("Missing required fields!")
            for field in [self.ui.name, self.ui.login, self.ui.password, self.ui.passwordRep]:
                if len(field.text()) == 0:
                    field.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))

    def upload(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("Images (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                mtcnn = MTCNN(image_size=1000, margin=0, min_face_size=20)  # initializing mtcnn for face detection
                img = Image.open(filenames[0])
                face, prob = mtcnn(img.resize((int(img.size[0] / 2), int(img.size[1] / 2))), return_prob=True)
                if face is None or prob < 0.95:
                    self.ui.uploadMes.setText("Your photo is not correct\nPlease, load another one")
                else:
                    self.ui.uploadMes.setText("OK! Now you can sigh in with your face!")
                    self.face_auth = True
                    copy(filenames[0], "user_data/face_photo.png")

    def back(self):
        self.close()
        self.sign_in.show()

    def reset_styles(self):
        self.ui.name.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.login.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.password.setStyleSheet(DEFAULT_LINE_STYLE)
        self.ui.passwordRep.setStyleSheet(DEFAULT_LINE_STYLE)

    @staticmethod
    def connect_to_db():
        return psycopg2.connect(host="127.0.0.1",
                                user="postgres",
                                password="1234567890",
                                database="app_users")
