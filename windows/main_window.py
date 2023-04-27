import psycopg2                                                           # PostgreSQL working lib
from PIL import Image                                                     # image class for networks
from PyQt6 import QtGui, QtCore                                           # PyQt packages
from PyQt6.QtCore import QPropertyAnimation                               # PyQt animation
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QDialog, QFileDialog  # PyQt ui classes
from ui.confirm_dialog import UiConfirm                                   # confirm window ui
from ui.main_menu import UiMainWindow                                     # main window ui
from ui.profile import UiProfile                                          # profile ui
from ui.settings import UiSettings                                        # settings ui
from windows.styles import *                                              # window styles and resources
from shutil import copy                                                   # function for copying photos
from facenet_pytorch import MTCNN                                         # network for face detection


# window for asking user ensurance
class Dialog(QDialog):
    def __init__(self, ok, cancel):
        super(Dialog, self).__init__()                                  # init QDialog class
        self.ui = UiConfirm()                                           # init confirm window ui
        self.ui.setupUi(self)                                           # setup ui
        self.ui.ok_button.clicked.connect(ok)                           # connect ok button
        self.ui.cancel_button.clicked.connect(cancel)                   # connect cancel button
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)   # set window type to hide title bar


# main window
class MainWindow(QMainWindow):
    def __init__(self, login):
        super(MainWindow, self).__init__()               # init QMainWindow class
        self.ui = UiMainWindow()                         # main window ui
        self.ui.setupUi(self)                            # setup main window ui
        self.profile = UiProfile()                       # init profile ui
        self.settings = UiSettings()                     # init settings ui
        MainWindow.setWindowTitle(self, f"{login}")      # set window title as user login
        self.ui.hello_title.setText(f"Hello, {login}!")  # set user greeting title
        # positioning window in the center of the screen
        qr = self.frameGeometry()                        # get window size
        cp = self.screen().availableGeometry().center()  # get center of screen
        qr.moveCenter(cp)                                # move window to the center
        self.move(qr.topLeft())                          #

        # connect buttons
        self.ui.button.clicked.connect(self.open_menu)        # open menu button
        self.ui.profile.clicked.connect(self.open_profile)    # open profile button
        self.ui.settings.clicked.connect(self.open_settings)  # open settings button

        # user data dictionary
        self.user_data = {"login": str, "password": str, "email": str, "name": str, "surname": str,
                          "user_photo": bytes, "face_photo": bytes, "face_auth": False}
        self.load_data(login)           # get data from database function
        self.settings_changed = None    # init settings flag
        self.animation = None           # init animation
        self.dialog = None              # init confirm dialog window

    # open navigation menu
    def open_menu(self):
        width = self.ui.slide_menu_cont.width()     # get current menu width
        # if current width = 0 -> menu is closed, setup new width for opening animation
        if width == 0:
            new_width = 170
            self.ui.button.setIcon(QtGui.QIcon(":/icons/icons/arrow_left.png"))
        # if current width = 170 -> menu is open, setup new width for closing animation
        else:
            new_width = 0
            self.ui.button.setIcon(QtGui.QIcon(":/icons/icons/menu.png"))

        # init and start animation
        self.animation = QPropertyAnimation(self.ui.slide_menu_cont, b"minimumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.start()

#   -- Profile ---
    # open user profile menu
    def open_profile(self):
        self.ui = self.profile  # change ui to profile
        self.ui.setupUi(self)   # setup new ui
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")  # set window title

        self.ui.name_line.setText(self.user_data["name"])                        # set name
        self.ui.surname_line.setText(self.user_data["surname"])                  # set surname
        self.ui.email_line.setText(self.user_data["email"])                      # set email
        self.ui.login_line.setText(self.user_data["login"])                      # set login
        self.ui.user_photo.setPixmap(QtGui.QPixmap("user_data/user_photo.png"))  # set user photo

        # connect buttons of new ui
        self.ui.chanhe_password.clicked.connect(self.change_password)        # opens field for entering new password
        self.ui.save_button.clicked.connect(self.save_data)                  # save info to users database
        self.ui.back.clicked.connect(self.back_to_main)                      # returns back to main window
        self.ui.exit_button.clicked.connect(self.exit_from_account)          # exit from user account
        self.ui.vis_button.clicked.connect(self.toggle_password_visibility)  # show/hide password
        self.ui.user_photo.installEventFilter(self)                          # upload user photo by icon click

    # upload profile photo by pressing on user photo
    def eventFilter(self, obj, event):
        # if mouse click on photo icon -> open file dialog to select new photo
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            # configure and open file dialog window
            dialog = QFileDialog(self)
            dialog.setDirectory(r'C:')
            dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            dialog.setNameFilter("Images (*.png *.jpg)")
            dialog.setViewMode(QFileDialog.ViewMode.List)
            # if file dialog window closed -> try to upload selected photo
            if dialog.exec():
                filename = dialog.selectedFiles()  # get path to selected file
                # if filename != None (file was selected) -> upload photo
                if filename:
                    copy(filename[0], "user_data/user_photo.png")       # copy selected image to user data
                    pixmap = QtGui.QPixmap("user_data/user_photo.png")  # setup selected image to user profile
                    self.profile.user_photo.setPixmap(pixmap)           #
                    # save selected image to users database
                    try:
                        connection = self.connect_to_db()    # establish connection to database
                        with connection.cursor() as cursor:  # init cursor to execute PostgreSQL command
                            drawing = open("user_data/user_photo.png", 'rb').read()
                            # update user photo by login
                            cursor.execute(f"update users " 
                                           f"set user_photo = {psycopg2.Binary(drawing)} "
                                           f"where login = '{self.user_data['login']}'")
                            connection.commit()              # commit changes
                        connection.close()                   # close connection
                    # processing database errors
                    except psycopg2.Error:
                        print("[INFO] database error")
        return False

    # opens field for entering new password
    def change_password(self):
        self.profile.change_frame.setMinimumHeight(0)       # hide password change button
        self.profile.change_frame.setMaximumHeight(0)       #
        self.profile.password_frame.setMaximumHeight(111)   # show lines for changing password
        self.profile.password2_frame.setMaximumHeight(111)  #

    # show/hide password
    def toggle_password_visibility(self):
        # if current password line echo mode = password (***) -> change to normal echo mode
        if self.profile.password_line.echoMode() == QLineEdit.EchoMode.Password:
            self.profile.password_line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.profile.password2_line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.profile.vis_button.setIcon(QtGui.QIcon(":/icons/icons/view.png"))
        # if current password line echo mode = normal -> change to password echo mode
        else:
            self.profile.password_line.setEchoMode(QLineEdit.EchoMode.Password)
            self.profile.password2_line.setEchoMode(QLineEdit.EchoMode.Password)
            self.profile.vis_button.setIcon(QtGui.QIcon(":/icons/icons/view_off.png"))

    # saving data to users database
    def save_data(self):
        name = self.profile.name_line.text()              # get new name
        surname = self.profile.surname_line.text()        # get new surname
        email = self.profile.email_line.text()            # get new email
        login = self.profile.login_line.text()            # get new login
        new_password = self.profile.password_line.text()  # get new password
        # if new password entered -> select new, else select password from user data
        new_password = new_password if len(new_password) > 0 else self.user_data["password"]

        # if OK pressed in dialog window -> save info to users database
        def ok_pressed():
            try:
                connection = self.connect_to_db()    # establish connection to database
                with connection.cursor() as cursor:  # init cursor to execute PostgreSQL command
                    # select login by login
                    cursor.execute(f"select login from users where login = '{login}'")
                    info = cursor.fetchone()         # receive query result
                    # if entered login in database, and it is not current user login -> inform user
                    if info is not None and info[0] != self.user_data["login"]:
                        self.profile.login_line.setText(OCCUPIED_LOGIN.replace(" already ", ' '))
                        self.profile.login_line.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
                    # if no such login in database or entered login = current user login -> update info in table
                    else:
                        self.profile.login_line.setStyleSheet(DEFAULT_LINE_STYLE)  # clean login style
                        # execute PostgreSQL command (update all user info)
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
                        connection.commit()  # commit changes in database

                        self.user_data["login"] = login                 # update current user data with entered fields
                        self.user_data["email"] = email                 #
                        self.user_data["name"] = name                   #
                        self.user_data["surname"] = surname             #
                        if new_password != self.user_data["password"]:  #
                            self.user_data["password"] = new_password   #
                connection.close()                                      # close connection
            # processing database errors
            except psycopg2.Error as _ex:
                print("[INFO] database working error")
            self.dialog.close()  # close confirm dialog window

        # if CANCEL pressed in dialog window -> close window
        def cancel_pressed():
            self.dialog.close()  # close confirm dialog window

        # open dialog window
        self.dialog = Dialog(ok_pressed, cancel_pressed)  # init confirm dialog window
        self.dialog.show()                                # show confirm dialog window

    # returns back to main menu
    def back_to_main(self):
        self.ui = UiMainWindow()  # change iu to main window
        self.ui.setupUi(self)     # setup new ui
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")      # setup window title
        self.ui.hello_title.setText(f"Hello, {self.user_data['login']}!")  # setup hello title

        # reconnect buttons of ui
        self.ui.button.clicked.connect(self.open_menu)        # open menu button
        self.ui.profile.clicked.connect(self.open_profile)    # open profile button
        self.ui.settings.clicked.connect(self.open_settings)  # open settings button

    # exit from account and close app window
    def exit_from_account(self):
        # if OK pressed in dialog window -> exit from user account
        def ok_pressed():
            self.dialog.close()
            # rewrite user data login file not auto log in next time
            with open("user_data/data.py", "w") as datafile:
                datafile.seek(0)
                datafile.write(f"logged = False\nlogin = ''\npassword = ''\n")
                datafile.truncate()
            self.close()

        # if CANCEL pressed in dialog window -> close window
        def cancel_pressed():
            self.dialog.close()

        self.dialog = Dialog(ok_pressed, cancel_pressed)  # init dialog window
        self.dialog.show()                                # show dialog window

#   --- Settings ---
    # open settings menu
    def open_settings(self):
        self.ui = self.settings  # change ui to settings
        self.ui.setupUi(self)    #
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")  # set window title

        # if user enable face auth previously -> instantly set checked enable button
        if self.user_data["face_auth"]:
            self.ui.enable_button.setChecked(True)

        # connect buttons of new gui
        self.ui.back_button.clicked.connect(self.save_and_back)       # return to main menu
        self.ui.enable_button.toggled.connect(self.toggle_face_auth)  # open upload menu
        self.ui.uploadButton.clicked.connect(self.upload_face)        # upload face photo

        self.settings_changed = False

    # face auth button pressed
    def toggle_face_auth(self):
        self.settings_changed = True
        # if face auth now enabled -> open upload button for user with animation
        if self.settings.enable_button.isChecked():
            # init and start opening animation
            self.animation = QPropertyAnimation(self.settings.upload_frame, b"maximumHeight")
            self.animation.setDuration(150)
            self.animation.setStartValue(0)
            self.animation.setEndValue(150)
            self.animation.start()
        # if face auth now disabled -> update user data and hide upload button
        else:
            self.user_data["face_auth"] = False
            self.settings.back_button.setEnabled(True)
            self.settings.upload_frame.setMaximumHeight(0)

    # upload button pressed
    def upload_face(self):
        # configure and open file dialog window
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("Images (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        # if file dialog window closed -> try to check uploaded image
        if dialog.exec():
            filename = dialog.selectedFiles()
            # if any file was selected -> check it for face
            if filename:
                mtcnn = MTCNN(image_size=1000, margin=0, min_face_size=20)  # initializing mtcnn for face detection
                img = Image.open(filename[0])
                face, prob = mtcnn(img, return_prob=True)                   # returns cropped face and probability
                # if face was not detected or ensurance of network < 95% -> inform user about incorrect photo
                if face is None or prob < 0.95:
                    self.settings.label.setText(INCORRECT_PHOTO)
                    self.settings.back_button.setEnabled(False)
                # if face was detected -> save photo to user data
                else:
                    self.settings.label.setText(OK_PHOTO)
                    self.user_data["face_auth"] = True
                    copy(filename[0], "user_data/face_photo.png")
                    self.settings.back_button.setEnabled(True)

    # back to main menu button pressed
    def save_and_back(self):
        # if settings changed flag was marked -> save changes to database
        if self.settings_changed:
            try:
                connection = self.connect_to_db()    # connect to database
                with connection.cursor() as cursor:  # init cursor
                    # update users database with face auth flag and user face photo
                    cursor.execute(f"update users "
                                   f"set enable_face_auth = {self.user_data['face_auth']}, "
                                   f"user_face = {psycopg2.Binary(open('user_data/face_photo.png', 'rb').read())} "
                                   f"where login = '{self.user_data['login']}'")
                    connection.commit()              # save changes to database
                connection.close()                   # close connection
            # processing database errors
            except psycopg2.Error as _ex:
                print("[INFO] database working error")
        self.back_to_main()

    # loading all user info from database
    def load_data(self, login):
        try:
            connect = self.connect_to_db()
            with connect.cursor() as cursor:
                cursor.execute(f"select * from users where login = '{login}'")
                info = cursor.fetchone()    # info[0] = user id
                self.user_data["name"] = info[1]
                self.user_data["surname"] = info[2]
                self.user_data["email"] = info[3]
                self.user_data["login"] = info[4]
                self.user_data["password"] = info[5]
                self.user_data["user_photo"] = info[6]
                self.user_data["face_auth"] = info[7]
                self.user_data["face_photo"] = info[8]
                # if user upload photo to database -> upload it to current user data
                if self.user_data["user_photo"] is not None:
                    with open("user_data/user_photo.png", "wb") as photo:
                        photo.write(bytes(self.user_data["user_photo"]))
                # if no user photo in database -> upload person icon as user photo
                else:
                    with open("user_data/user_photo.png", "wb") as photo, open("ui/icons/person.png", "rb") as a:
                        photo_b = a.read()
                        photo.write(photo_b)
                # if user upload face in database -> upload it to current user data
                if self.user_data.get("face_photo") is not None:
                    with open("user_data/face_photo.png", "wb") as photo:
                        photo.write(bytes(self.user_data["face_photo"]))
                # if no user face in database -> upload person icon as user face
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
