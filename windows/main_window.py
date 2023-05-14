"""
File that implements all methods for Main Menu window correct working.
"""

import psycopg2                                                           # PostgreSQL working lib
from PIL import Image, ImageDraw                                          # image class for networks
from PyQt6.QtCore import QPropertyAnimation, QUrl, Qt, QEvent             # PyQt
from PyQt6.QtGui import QDesktopServices, QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QDialog, QFileDialog  # PyQt ui classes
from ui.about import UiAbout                                              # about window ui
from ui.confirm_dialog import UiConfirm                                   # confirm window ui
from ui.main_menu import UiMainWindow                                     # main window ui
from ui.profile import UiProfile                                          # profile ui
from ui.settings import UiSettings                                        # settings ui
from windows import connect_to_db
from windows.styles import *                                              # window styles and resources
from shutil import copy                                                   # function for copying photos
from facenet_pytorch import MTCNN                                         # network for face detection


# window for asking user ensurance
class Dialog(QDialog):
    """
    Backend of confirm dialog window.
    """
    def __init__(self, ok, cancel):
        """
        Initialization of confirm dialog window.
        :param ok: function that connects to "OK" button.
        :param cancel: function that connects to "Cancel" button.
        """
        super(Dialog, self).__init__()                                  # init QDialog class
        self.ui = UiConfirm()                                           # init confirm window ui
        self.ui.setupUi(self)                                           # setup ui
        self.ui.ok_button.clicked.connect(ok)                           # connect ok button
        self.ui.cancel_button.clicked.connect(cancel)                   # connect cancel button
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)   # set window type to hide title bar


# main window
class MainWindow(QMainWindow):
    """
    Backend of Main Menu window.

    This class implements methods for main menu window working.
    """
    def __init__(self, login):
        """
        Initializing of Main Menu window.

        This method initialize user interface, local variables and connect buttons with methods.
        :param login: user login used in sign in procedure.
        """
        super(MainWindow, self).__init__()               # init QMainWindow class
        self.main = UiMainWindow()
        self.ui = self.main                              # main window ui
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
        self.setup_main_buttons()

        # user data dictionary
        self.user_data = {"login": str, "password": str, "email": str, "name": str, "surname": str,
                          "user_photo": bytes, "face_photo": bytes, "face_auth": False}
        self.load_data(login)           # get data from database function
        self.settings_changed = None    # init settings flag
        self.animation = None           # init animation
        self.dialog = None              # init confirm dialog window

    def setup_main_buttons(self):
        """
        Set methods for processing button clicks on every ui button.
        """
        self.ui.button.clicked.connect(self.open_menu)        # open menu button
        self.ui.profile.clicked.connect(self.open_profile)    # open profile button
        self.ui.settings.clicked.connect(self.open_settings)  # open settings button
        self.ui.about.clicked.connect(self.open_about)        # open about button
        self.ui.close_menu_button.clicked.connect(self.close_menu)    # close menu button
        self.ui.button_2.clicked.connect(self.open_menu)      # open menu button
        self.ui.uploadButton.clicked.connect(self.face_auth_test)  # select image and detect face

    # open navigation menu
    def open_menu(self):
        """
        Method for changing navigation menu width.

        If menu is open -> close it.

        If menu is half open -> open it fully.

        If menu is fully closed -> open it fully.
        """
        width = self.ui.slide_menu_cont.width()     # get current menu width
        # if current width = 0 -> menu is closed, setup new width for opening animation
        if self.ui.image_output.minimumWidth() != 0:
            return
        if width == 60 or width == 0:
            if width == 0:
                self.ui.button_2.setMinimumWidth(0)
            new_width = 170
            self.ui.button.setIcon(QIcon(":/icons/icons/arrow_left.svg"))
            # show text on buttons
            self.ui.menu_label.setMinimumWidth(120)
            self.ui.profile.setMinimumWidth(150)
            self.ui.profile.setText(" Profile")
            self.ui.settings.setMinimumWidth(150)
            self.ui.settings.setText(" Settings")
            self.ui.about.setMinimumWidth(150)
            self.ui.about.setText(" About")
            self.ui.close_menu_button.setMinimumWidth(100)
            self.ui.close_menu_button.setText(" Close")
        # if current width = 170 -> menu is open, setup new width for closing animation
        else:
            new_width = 60
            self.ui.button.setIcon(QIcon(":/icons/icons/menu.svg"))
            # hide text on buttons
            self.ui.menu_label.setMinimumWidth(0)
            self.ui.profile.setMinimumWidth(40)
            self.ui.profile.setText("")
            self.ui.settings.setMinimumWidth(40)
            self.ui.settings.setText("")
            self.ui.about.setMinimumWidth(40)
            self.ui.about.setText("")
            self.ui.close_menu_button.setMinimumWidth(40)
            self.ui.close_menu_button.setText("")

        # init and start animation
        self.animation = QPropertyAnimation(self.ui.slide_menu_cont, b"maximumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.start()
        self.ui.slide_menu.setMaximumWidth(170)

    # close menu button pressed
    def close_menu(self):
        """
        Method for fully closing navigation menu.
        """
        # set menu width = 0
        self.ui.slide_menu_cont.setMinimumWidth(0)
        self.ui.slide_menu_cont.setMaximumWidth(0)
        self.ui.slide_menu.setMaximumWidth(0)
        self.ui.slide_menu.setMinimumWidth(0)
        self.ui.button_2.setMinimumWidth(40)

    # upload button pressed -> open upload dialog, detect face on selected image, output
    def face_auth_test(self):
        """
        Method for processing mouse click on "Upload" button in main menu user interface.

        This method ask user to upload image and then try to detect face. Finally, output result for user.
        """
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
                mtcnn = MTCNN(image_size=1000, keep_all=True, min_face_size=100)   # init detection model
                img = Image.open(filename[0])
                boxes, probs, points = mtcnn.detect(img, landmarks=True)  # get face boxes and probabilities
                # if any face detected -> mark them on image and output to user
                if probs[0] is not None:
                    img_draw = img.copy()
                    draw = ImageDraw.Draw(img_draw)
                    for i, (box, point) in enumerate(zip(boxes, points)):
                        draw.rectangle(box.tolist(), width=5)
                        for p in point:
                            draw.rectangle((p - 5).tolist() + (p + 5).tolist(), width=8)
                    img_draw.save('user_data/detected_faces.png')
                    # output image on main window
                    image = QPixmap('user_data/detected_faces.png')
                    if image.width() > 665 or image.height() > 576:
                        image = image.scaled(665, 576, Qt.AspectRatioMode.KeepAspectRatio)
                    self.ui.image_output.setMinimumWidth(1)
                    self.ui.image_output.setMaximumWidth(image.width())
                    self.ui.image_output.setMaximumHeight(image.height())
                    self.ui.image_output.setStyleSheet("border: 2px solid #000000;\n"
                                                       "border-radius: 0px;")
                    self.ui.image_output.setPixmap(image)
                # if no face detected -> inform user
                else:
                    self.ui.image_output.setText("Cannot detect any faces on selected image")

#   -- Profile ---
    # open user profile menu
    def open_profile(self):
        """
        Method for processing mouse click on "Profile" button in navigation menu.

        Method opens user profile interface, connect buttons and paste user info in relevant lines.
        """
        self.ui = self.profile  # change ui to profile
        self.ui.setupUi(self)   # setup new ui
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")  # set window title

        self.ui.name_line.setText(self.user_data["name"])                        # set name
        self.ui.surname_line.setText(self.user_data["surname"])                  # set surname
        self.ui.email_line.setText(self.user_data["email"])                      # set email
        self.ui.login_line.setText(self.user_data["login"])                      # set login
        self.ui.user_photo.setPixmap(QPixmap("user_data/user_photo.png"))  # set user photo

        # connect buttons of new ui
        self.ui.change_password.clicked.connect(self.change_password)        # opens field for entering new password
        self.ui.save_button.clicked.connect(self.save_data)                  # save info to users database
        self.ui.back.clicked.connect(self.back_to_main)                      # returns back to main window
        self.ui.exit_button.clicked.connect(self.exit_from_account)          # exit from user account
        self.ui.vis_button.clicked.connect(self.toggle_password_visibility)  # show/hide password
        self.ui.user_photo.installEventFilter(self)                          # upload user photo by icon click

    # upload profile photo by pressing on user photo
    def eventFilter(self, obj, event):
        """
        Method for processing mouse click on "User avatar image" in profile user interface.

        This method ask user to upload new user profile image.
        """
        # if mouse click on photo icon -> open file dialog to select new photo
        if event.type() == QEvent.Type.MouseButtonPress:
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
                    pixmap = QPixmap("user_data/user_photo.png")  # setup selected image to user profile
                    self.profile.user_photo.setPixmap(pixmap)           #
                    # save selected image to users database
                    try:
                        connection = connect_to_db()    # establish connection to database
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
        """
        Method for processing mouse click on "Change password" button in profile user interface.

        This method show in interface fields where user should input new password.
        """
        self.profile.change_frame.setMinimumHeight(0)       # hide password change button
        self.profile.change_frame.setMaximumHeight(0)       #
        self.profile.password_frame.setMaximumHeight(111)   # show lines for changing password
        self.profile.password2_frame.setMaximumHeight(111)  #

    # show/hide password
    def toggle_password_visibility(self):
        """
        Method for processing mouse click on "Visibility" button in profile user interface.

        This method toggle passwords line echo mode (password/normal).
        """
        # if current password line echo mode = password (***) -> change to normal echo mode
        if self.profile.password_line.echoMode() == QLineEdit.EchoMode.Password:
            self.profile.password_line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.profile.password2_line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.profile.vis_button.setIcon(QIcon(":/icons/icons/view.svg"))
        # if current password line echo mode = normal -> change to password echo mode
        else:
            self.profile.password_line.setEchoMode(QLineEdit.EchoMode.Password)
            self.profile.password2_line.setEchoMode(QLineEdit.EchoMode.Password)
            self.profile.vis_button.setIcon(QIcon(":/icons/icons/view_off.svg"))

    # saving data to users database
    def save_data(self):
        """
        Method for processing mouse click on "Save" button in profile user interface.

        This method generates dialog window to ask user "Are you sure?" and implements functions of user answer.
        """
        name = self.profile.name_line.text()              # get new name
        surname = self.profile.surname_line.text()        # get new surname
        email = self.profile.email_line.text()            # get new email
        login = self.profile.login_line.text()            # get new login
        new_password = self.profile.password_line.text()  # get new password
        new_password_rep = self.profile.password2_line.text()
        # if new password entered -> select new, else select password from user data
        new_password = new_password if len(new_password) > 0 else self.user_data["password"]
        new_password_rep = new_password_rep if len(new_password_rep) > 0 else self.user_data["password"]

        # if OK pressed in dialog window -> save info to users database
        def ok_pressed():
            """
            Function for processing "OK" button in confirm dialog window.

            This function execute SQL command to save input lines in user database.
            """
            try:
                connection = connect_to_db()    # establish connection to database
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
            """
            Function for processing "Cancel" button in confirm dialog window.

            This function just close dialog window.
            """
            self.dialog.close()  # close confirm dialog window

        if new_password == new_password_rep:
            # open dialog window
            self.dialog = Dialog(ok_pressed, cancel_pressed)  # init confirm dialog window
            self.dialog.show()                                # show confirm dialog window
        else:
            self.profile.password_line.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))
            self.profile.password2_line.setStyleSheet(DEFAULT_LINE_STYLE.replace(BLACK, RED))

    # returns back to main menu
    def back_to_main(self):
        """
        Method for processing "Back" button in profile user interface.

        This method change user interface and connect buttons for main menu.
        """
        self.ui = self.main       # change iu to main window
        self.ui.setupUi(self)     # setup new ui
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")      # setup window title
        self.ui.hello_title.setText(f"Hello, {self.user_data['login']}!")  # setup hello title

        # reconnect buttons of ui
        self.setup_main_buttons()

    # exit from account and close app window
    def exit_from_account(self):
        """
        Method for processing mouse click on "Exit" button in profile user interface.

        This method generates dialog window to ask user "Are you sure?" and implements functions of user answer.
        """
        # if OK pressed in dialog window -> exit from user account
        def ok_pressed():
            """
            Function for processing "OK" button in confirm dialog window.

            This function exit from user account and close application window.
            """
            self.dialog.close()
            # rewrite user data login file not auto log in next time
            with open("user_data/data.py", "w") as datafile:
                datafile.seek(0)
                datafile.write(f"logged = False\nlogin = ''\npassword = ''\n")
                datafile.truncate()
            self.close()

        # if CANCEL pressed in dialog window -> close window
        def cancel_pressed():
            """
            Function for processing "Cancel" button in confirm dialog window.

            This function just close dialog window.
            """
            self.dialog.close()

        self.dialog = Dialog(ok_pressed, cancel_pressed)  # init dialog window
        self.dialog.show()                                # show dialog window

#   --- Settings ---
    # open settings menu
    def open_settings(self):
        """
        Method for processing mouse click on "Settings" button in navigation menu.

        Method opens settings interface and connect buttons of settings menu.
        """
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
        """
        Method for processing mouse click on checkbox "Face authentication" in settings menu.

        If it is now enabled -> open upload button for user.

        If it is now disabled -> set up face auth flag = false.
        """
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
        """
        Method for processing mouse click on "Upload" button in settings menu.

        Ask user to select image with his face, try to construct user face pattern from selected image.
        """
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
                mtcnn = MTCNN(image_size=160, margin=0, min_face_size=10)  # initializing mtcnn for face detection
                img = Image.open(filename[0])
                face, prob = mtcnn(img, return_prob=True, save_path="user_data/face_photo.png")
                # if face was not detected or ensurance of network < 95% -> inform user about incorrect photo
                if face is None or prob < 0.95:
                    self.settings.label.setText(INCORRECT_PHOTO)
                    self.settings.back_button.setEnabled(False)
                # if face was detected -> save photo to user data
                else:
                    self.settings.label.setText(OK_PHOTO)
                    self.user_data["face_auth"] = True
                    self.settings.back_button.setEnabled(True)

    # back to main menu button pressed
    def save_and_back(self):
        """
        Method for processing mouse click on "Back" button in settings menu.

        If some settings changed -> save data to user database.

        Returns user back to main menu.
        """
        # if settings changed flag was marked -> save changes to database
        if self.settings_changed:
            try:
                connection = connect_to_db()    # connect to database
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

#   --- About ---
    def open_about(self):
        """
        Method for processing mouse click on "About" button in navigation menu.

        Method opens about interface and connect buttons of about menu.
        """
        self.ui = UiAbout()       # change iu to main window
        self.ui.setupUi(self)     # setup new ui
        MainWindow.setWindowTitle(self, f"{self.user_data['login']}")      # setup window title

        # reconnect buttons of ui
        self.ui.back_button.clicked.connect(self.back_to_main)
        self.ui.github_button.clicked.connect(self.open_github)

    @staticmethod
    def open_github():
        """
        Method for processing mouse click on GitHub icon in about menu.

        Open GitHub repository of project.
        """
        QDesktopServices.openUrl(QUrl("https://github.com/shmatozz/desktop-App-With-Face-Auth"))

    # loading all user info from database
    def load_data(self, login):
        """
        Method for get user information from database.

        Called in __init__ method.
        :param login: user login used to sign in app.
        """
        try:
            connect = connect_to_db()
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
