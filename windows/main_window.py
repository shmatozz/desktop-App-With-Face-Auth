import psycopg2
from PIL import Image
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QDialog, QFileDialog
from ui.confirm_dialog import UiConfirm
from ui.mainActivity import UiMainWindow
from ui.profile import UiProfile
from ui.settings import UiSettings
from windows.styles import *
from shutil import copy
from facenet_pytorch import MTCNN


class Dialog(QDialog):
    def __init__(self, ok, cancel):
        super(Dialog, self).__init__()
        self.ui = UiConfirm()
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(ok)
        self.ui.cancel_button.clicked.connect(cancel)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AttributeCount)


class MainWindow(QMainWindow):
    def __init__(self, login):
        super(MainWindow, self).__init__()
        self.ui = UiMainWindow()  # main window ui
        self.ui.setupUi(self)
        self.profile = UiProfile()  # profile ui
        self.settings = UiSettings()
        MainWindow.setWindowTitle(self, f"{login}")
        self.ui.hello_title.setText(f"Hello, {login}!")
        # positioning window in the center of the screen
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # connect buttons
        self.ui.button.clicked.connect(self.open_menu)
        self.ui.profile.clicked.connect(self.open_profile)
        self.ui.settings.clicked.connect(self.open_settings)

        # some user data
        self.user_data = {"login": str, "password": str, "email": str, "name": str, "surname": str,
                          "user_photo": bytes, "face_photo": bytes, "face_auth": False}
        self.load_data(login)
        self.settings_changed = None
        self.animation = None
        self.dialog = None

    # open navigation menu
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
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")

        self.ui.name_line.setText(self.user_data["name"])  # set name
        self.ui.surname_line.setText(self.user_data["surname"])  # set surname
        self.ui.email_line.setText(self.user_data["email"])  # set email
        self.ui.login_line.setText(self.user_data["login"])  # set login
        self.ui.user_photo.setPixmap(QPixmap("user_data/user_photo.png"))
        self.ui.user_photo.setStyleSheet("border-radius: 0px;\nborder: 2px solid #000000;")

        # connect buttons of new ui
        self.ui.chanhe_password.clicked.connect(self.change_password)  # opens field for entering new password
        self.ui.save_button.clicked.connect(self.save_data)  # save info to users database
        self.ui.back.clicked.connect(self.back_to_main)  # returns back to main window
        self.ui.exit_button.clicked.connect(self.exit_from_account)  # exit from user account
        self.ui.vis_button.clicked.connect(self.toggle_password_visibility)  # show/hide password
        self.ui.user_photo.installEventFilter(self)  # upload photo

    # upload profile photo
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            dialog = QFileDialog(self)
            dialog.setDirectory(r'C:')
            dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            dialog.setNameFilter("Images (*.png *.jpg)")
            dialog.setViewMode(QFileDialog.ViewMode.List)
            if dialog.exec():
                filenames = dialog.selectedFiles()
                if filenames:
                    copy(filenames[0], "user_data/user_photo.png")
                    pixmap = QPixmap("user_data/user_photo.png")
                    self.profile.user_photo.setPixmap(pixmap)
                    try:
                        connection = self.connect_to_db()

                        with connection.cursor() as cursor:
                            drawing = open("user_data/user_photo.png", 'rb').read()

                            cursor.execute(f"update users "
                                           f"set user_photo = {psycopg2.Binary(drawing)} "
                                           f"where login = '{self.user_data['login']}'")
                            connection.commit()

                        connection.close()
                    except psycopg2.Error:
                        print("[INFO] database error")

        return False

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
        new_password = new_password if len(new_password) > 0 else self.user_data["password"]

        # if OK pressed in dialog window -> save info to users database
        def ok_pressed():
            try:
                # connect to database
                connection = self.connect_to_db()
                with connection.cursor() as cursor:
                    cursor.execute(f"select login from users where login = '{login}'")
                    info = cursor.fetchone()
                    if info is not None and info[0] != self.user_data["login"]:
                        self.profile.login_line.setText("Login is occupied!")
                        self.profile.login_line.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
                    else:
                        self.profile.login_line.setStyleSheet(DEFAULT_LINE_STYLE)
                        cursor.execute(f"update users "
                                       f"set user_name = '{name.capitalize()}', "
                                       f"surname = '{surname.capitalize()}', "
                                       f"email = '{email}', "
                                       f"login = '{login}', "
                                       f"password = '{new_password}', "
                                       f"user_photo = {psycopg2.Binary(open('user_data/user_photo.png', 'rb').read())},"
                                       f" enable_face_auth = {self.user_data['face_auth']}, "
                                       f"user_face = {psycopg2.Binary(open('user_data/face_photo.png', 'rb').read())} "
                                       f"where login = '{self.user_data['login']}'")
                        connection.commit()

                        self.user_data["login"] = login
                        self.user_data["email"] = email
                        self.user_data["name"] = name
                        self.user_data["surname"] = surname
                        if new_password != self.user_data["password"]:
                            self.user_data["password"] = new_password

                # close connection
                connection.close()
            except psycopg2.Error as _ex:
                print("[INFO] database working error")
            self.dialog.close()

        # if CANCEL pressed in dialog window -> close window
        def cancel_pressed():
            self.dialog.close()

        # open dialog window
        print(1)
        self.dialog = Dialog(ok_pressed, cancel_pressed)
        self.dialog.show()

    # returns back to main menu
    def back_to_main(self):
        # change ui
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")

        self.ui.hello_title.setText(f"Hello, {self.user_data['login']}!")

        # connect buttons of new ui
        self.ui.button.clicked.connect(self.open_menu)
        self.ui.profile.clicked.connect(self.open_profile)
        self.ui.settings.clicked.connect(self.open_settings)

    # exit from account to sing in menu
    def exit_from_account(self):
        # if OK pressed in dialog window -> exit from user account
        def ok_pressed():
            self.dialog.close()
            with open("user_data/data.py", "w") as datafile:
                datafile.seek(0)
                datafile.write(f"logged = False\nlogin = ''\npassword = ''\n")
                datafile.truncate()

            self.close()

        # if CANCEL pressed in dialog window -> close window
        def cancel_pressed():
            self.dialog.close()

        self.dialog = Dialog(ok_pressed, cancel_pressed)
        self.dialog.show()

    # Settings =======================================================================
    # open settings menu
    def open_settings(self):
        # setup interface
        self.ui = self.settings
        self.ui.setupUi(self)
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")

        if self.user_data["face_auth"]:
            self.ui.enable_button.setChecked(True)

        # connect buttons of new gui
        self.ui.back_button.clicked.connect(self.save_and_back)  # return to main menu
        self.ui.enable_button.toggled.connect(self.toggle_face_auth)  # open upload menu
        self.ui.uploadButton.clicked.connect(self.upload_face)  # upload face photo

        self.settings_changed = False

    def toggle_face_auth(self):
        self.settings_changed = True
        if self.settings.enable_button.isChecked():
            self.animation = QPropertyAnimation(self.settings.upload_frame, b"maximumHeight")
            self.animation.setDuration(150)
            self.animation.setStartValue(0)
            self.animation.setEndValue(150)
            self.animation.start()
        else:
            self.user_data["face_auth"] = False
            self.settings.back_button.setEnabled(True)
            self.settings.upload_frame.setMaximumHeight(0)
        pass

    def upload_face(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("Images (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                mtcnn = MTCNN(image_size=250, margin=0, min_face_size=20)  # initializing mtcnn for face detection
                img = Image.open(filenames[0])
                face, prob = mtcnn(img, return_prob=True)  # returns cropped face and probability
                if face is None or prob < 0.95:
                    self.settings.label.setText("Your photo is not correct\nPlease, load another one")
                    self.settings.back_button.setEnabled(False)
                else:
                    self.settings.label.setText("OK! Now you can sigh in with your face!")
                    self.user_data["face_auth"] = True
                    copy(filenames[0], "user_data/face_photo.png")
                    self.settings.back_button.setEnabled(True)

    def save_and_back(self):
        if self.settings_changed:
            try:
                # connect to database
                connection = self.connect_to_db()

                with connection.cursor() as cursor:
                    cursor.execute(f"update users "
                                   f"set enable_face_auth = {self.user_data['face_auth']}, "
                                   f"user_face = {psycopg2.Binary(open('user_data/face_photo.png', 'rb').read())} "
                                   f"where login = '{self.user_data['login']}'")
                    connection.commit()

                # close connection
                connection.close()
            except psycopg2.Error as _ex:
                print("[INFO] database working error")

        self.back_to_main()

    # ====================================================

    # loading user profile image from data base
    def load_data(self, login):
        try:
            connect = self.connect_to_db()

            with connect.cursor() as cursor:
                cursor.execute(f"select * from users where login = '{login}'")
                info = cursor.fetchone()
                self.user_data["name"] = info[1]
                self.user_data["surname"] = info[2]
                self.user_data["email"] = info[3]
                self.user_data["login"] = info[4]
                self.user_data["password"] = info[5]
                self.user_data["user_photo"] = info[6]
                self.user_data["face_auth"] = info[7]
                self.user_data["face_photo"] = info[8]
                if self.user_data["user_photo"] is not None:
                    with open("user_data/user_photo.png", "wb") as photo:
                        photo.write(bytes(self.user_data["user_photo"]))
                else:
                    with open("user_data/user_photo.png", "wb") as photo, open("ui/icons/person.png", "rb") as a:
                        photo_b = a.read()
                        photo.write(photo_b)
                if self.user_data.get("face_photo") is not None:
                    with open("user_data/face_photo.png", "wb") as photo:
                        photo.write(bytes(self.user_data["face_photo"]))
                else:
                    with open("user_data/face_photo.png", "wb") as photo, open("ui/icons/person.png", "rb") as a:
                        photo_b = a.read()
                        photo.write(photo_b)

            connect.close()
        except psycopg2.Error:
            print("[INFO] database error")

    # establish connection to database
    @staticmethod
    def connect_to_db():
        return psycopg2.connect(host="127.0.0.1",
                                user="postgres",
                                password="1234567890",
                                database="app_users")
