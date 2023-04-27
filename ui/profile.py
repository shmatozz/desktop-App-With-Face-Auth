from PyQt6 import QtCore, QtGui, QtWidgets


class UiProfile(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.profile_photo = QtWidgets.QFrame(parent=self.centralwidget)
        self.profile_photo.setMinimumSize(QtCore.QSize(200, 0))
        self.profile_photo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.profile_photo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.profile_photo.setObjectName("profile_photo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.profile_photo)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.photo = QtWidgets.QFrame(parent=self.profile_photo)
        self.photo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.photo.setObjectName("photo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.photo)
        self.verticalLayout_3.setContentsMargins(11, 15, 11, 11)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.user_photo = QtWidgets.QLabel(parent=self.photo)
        self.user_photo.setMinimumSize(QtCore.QSize(200, 200))
        self.user_photo.setMaximumSize(QtCore.QSize(200, 200))
        self.user_photo.setStyleSheet("border-radius: 0px;\n"
                                      "border: 2px solid #000000;")
        self.user_photo.setText("")
        self.user_photo.setPixmap(QtGui.QPixmap(":/icons/icons/person.png"))
        self.user_photo.setScaledContents(True)
        self.user_photo.setObjectName("user_photo")
        self.verticalLayout_3.addWidget(self.user_photo)
        self.exit_frame = QtWidgets.QFrame(parent=self.photo)
        self.exit_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.exit_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.exit_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.exit_frame.setObjectName("exit_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.exit_frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.exit_button = QtWidgets.QPushButton(parent=self.exit_frame)
        self.exit_button.setMaximumSize(QtCore.QSize(100, 40))
        self.exit_button.setStyleSheet("QPushButton {\n"
                                       "    font: 75 16pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 0, 0);\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #000000;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    font: 75 16pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(234, 0, 0);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #000000;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    font: 75 16pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color:rgb(182, 0, 0);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #000000;\n"
                                       "}")
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_11.addWidget(self.exit_button)
        self.verticalLayout_3.addWidget(self.exit_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.photo)
        self.back_button = QtWidgets.QFrame(parent=self.profile_photo)
        self.back_button.setMinimumSize(QtCore.QSize(0, 111))
        self.back_button.setMaximumSize(QtCore.QSize(16777215, 111))
        self.back_button.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.back_button.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.back_button)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back = QtWidgets.QPushButton(parent=self.back_button)
        self.back.setMaximumSize(QtCore.QSize(100, 40))
        self.back.setStyleSheet("QPushButton {\n"
                                "    font: 75 16pt \"Bahnschrift\";\n"
                                "    color: rgb(120, 183, 140);\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                "    border-radius: 10px;\n"
                                "    border: 2px solid #000000;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "    font: 75 16pt \"Bahnschrift\";\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(100, 183, 140);\n"
                                "    border-radius: 10px;\n"
                                "    border: 2px solid #000000;\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed{\n"
                                "    font: 75 16pt \"Bahnschrift\";\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(88, 162, 123);\n"
                                "    border-radius: 10px;\n"
                                "    border: 2px solid #000000;\n"
                                "}")
        self.back.setObjectName("back")
        self.horizontalLayout_2.addWidget(self.back)
        self.verticalLayout.addWidget(self.back_button)
        self.horizontalLayout.addWidget(self.profile_photo, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(540, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_frame = QtWidgets.QFrame(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.name_frame.setFont(font)
        self.name_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.name_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 33, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.name_title = QtWidgets.QLabel(parent=self.name_frame)
        self.name_title.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.name_title.setFont(font)
        self.name_title.setObjectName("name_title")
        self.horizontalLayout_3.addWidget(self.name_title)
        self.name_line = QtWidgets.QLineEdit(parent=self.name_frame)
        self.name_line.setMinimumSize(QtCore.QSize(380, 0))
        self.name_line.setMaximumSize(QtCore.QSize(380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.name_line.setFont(font)
        self.name_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 10px;\n"
                                     "border: 2px solid #000000;\n"
                                     "padding-left: 20px\n"
                                     "")
        self.name_line.setMaxLength(20)
        self.name_line.setClearButtonEnabled(True)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout_3.addWidget(self.name_line)
        self.verticalLayout_2.addWidget(self.name_frame)
        self.surname_frame = QtWidgets.QFrame(parent=self.frame)
        self.surname_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.surname_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.surname_frame.setObjectName("surname_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.surname_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 33, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.surname_title = QtWidgets.QLabel(parent=self.surname_frame)
        self.surname_title.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.surname_title.setFont(font)
        self.surname_title.setStyleSheet("font: Bahnschrift")
        self.surname_title.setObjectName("surname_title")
        self.horizontalLayout_4.addWidget(self.surname_title)
        self.surname_line = QtWidgets.QLineEdit(parent=self.surname_frame)
        self.surname_line.setMinimumSize(QtCore.QSize(380, 0))
        self.surname_line.setMaximumSize(QtCore.QSize(380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.surname_line.setFont(font)
        self.surname_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "border: 2px solid #000000;\n"
                                        "padding-left: 20px\n"
                                        "")
        self.surname_line.setMaxLength(20)
        self.surname_line.setClearButtonEnabled(True)
        self.surname_line.setObjectName("surname_line")
        self.horizontalLayout_4.addWidget(self.surname_line)
        self.verticalLayout_2.addWidget(self.surname_frame)
        self.email_frame = QtWidgets.QFrame(parent=self.frame)
        self.email_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.email_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.email_frame.setObjectName("email_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.email_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 33, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.email_title = QtWidgets.QLabel(parent=self.email_frame)
        self.email_title.setMinimumSize(QtCore.QSize(100, 0))
        self.email_title.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.email_title.setFont(font)
        self.email_title.setObjectName("email_title")
        self.horizontalLayout_5.addWidget(self.email_title)
        self.email_line = QtWidgets.QLineEdit(parent=self.email_frame)
        self.email_line.setMinimumSize(QtCore.QSize(380, 60))
        self.email_line.setMaximumSize(QtCore.QSize(380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.email_line.setFont(font)
        self.email_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "border: 2px solid #000000;\n"
                                      "padding-left: 20px\n"
                                      "")
        self.email_line.setMaxLength(50)
        self.email_line.setClearButtonEnabled(True)
        self.email_line.setObjectName("email_line")
        self.horizontalLayout_5.addWidget(self.email_line)
        self.verticalLayout_2.addWidget(self.email_frame)
        self.login_frame = QtWidgets.QFrame(parent=self.frame)
        self.login_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.login_frame.setObjectName("login_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.login_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 33, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.login_title = QtWidgets.QLabel(parent=self.login_frame)
        self.login_title.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.login_title.setFont(font)
        self.login_title.setObjectName("login_title")
        self.horizontalLayout_6.addWidget(self.login_title)
        self.login_line = QtWidgets.QLineEdit(parent=self.login_frame)
        self.login_line.setMaximumSize(QtCore.QSize(380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.login_line.setFont(font)
        self.login_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "border: 2px solid #000000;\n"
                                      "padding-left: 20px\n"
                                      "")
        self.login_line.setMaxLength(20)
        self.login_line.setClearButtonEnabled(True)
        self.login_line.setObjectName("login_line")
        self.horizontalLayout_6.addWidget(self.login_line)
        self.verticalLayout_2.addWidget(self.login_frame)
        self.password_frame = QtWidgets.QFrame(parent=self.frame)
        self.password_frame.setMaximumSize(QtCore.QSize(16777215, 0))
        self.password_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.password_frame.setObjectName("password_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.password_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.password_title = QtWidgets.QLabel(parent=self.password_frame)
        self.password_title.setMinimumSize(QtCore.QSize(120, 0))
        self.password_title.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.password_title.setFont(font)
        self.password_title.setObjectName("password_title")
        self.horizontalLayout_7.addWidget(self.password_title)
        self.password_line = QtWidgets.QLineEdit(parent=self.password_frame)
        self.password_line.setMaximumSize(QtCore.QSize(380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.password_line.setFont(font)
        self.password_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;\n"
                                         "border: 2px solid #000000;\n"
                                         "padding-left: 20px\n"
                                         "")
        self.password_line.setMaxLength(20)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_line.setClearButtonEnabled(True)
        self.password_line.setObjectName("password_line")
        self.horizontalLayout_7.addWidget(self.password_line)
        self.vis_button = QtWidgets.QPushButton(parent=self.password_frame)
        self.vis_button.setMaximumSize(QtCore.QSize(25, 25))
        self.vis_button.setStyleSheet("QPushButton {\n"
                                      "    font: 75 16pt \"Bahnschrift\";\n"
                                      "    color: rgb(120, 183, 140);\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "    border: 1px solid #000000;\n"
                                      "}\n"
                                      "")
        self.vis_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/view_off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.vis_button.setIcon(icon)
        self.vis_button.setObjectName("vis_button")
        self.horizontalLayout_7.addWidget(self.vis_button)
        self.verticalLayout_2.addWidget(self.password_frame)
        self.password2_frame = QtWidgets.QFrame(parent=self.frame)
        self.password2_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.password2_frame.setMaximumSize(QtCore.QSize(16777215, 0))
        self.password2_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.password2_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.password2_frame.setObjectName("password2_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.password2_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 33, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.password2_title = QtWidgets.QLabel(parent=self.password2_frame)
        self.password2_title.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.password2_title.setFont(font)
        self.password2_title.setObjectName("password2_title")
        self.horizontalLayout_8.addWidget(self.password2_title)
        self.password2_line = QtWidgets.QLineEdit(parent=self.password2_frame)
        self.password2_line.setMaximumSize(QtCore.QSize(380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        self.password2_line.setFont(font)
        self.password2_line.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px;\n"
                                          "border: 2px solid #000000;\n"
                                          "padding-left: 20px\n"
                                          "")
        self.password2_line.setMaxLength(20)
        self.password2_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password2_line.setObjectName("password2_line")
        self.horizontalLayout_8.addWidget(self.password2_line)
        self.verticalLayout_2.addWidget(self.password2_frame)
        self.change_frame = QtWidgets.QFrame(parent=self.frame)
        self.change_frame.setMinimumSize(QtCore.QSize(0, 222))
        self.change_frame.setMaximumSize(QtCore.QSize(16777215, 222))
        self.change_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.change_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.change_frame.setObjectName("change_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.change_frame)
        self.horizontalLayout_9.setContentsMargins(0, 13, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.chanhe_password = QtWidgets.QPushButton(parent=self.change_frame)
        self.chanhe_password.setMinimumSize(QtCore.QSize(250, 40))
        self.chanhe_password.setMaximumSize(QtCore.QSize(250, 40))
        self.chanhe_password.setStyleSheet("QPushButton {\n"
                                           "    font: 75 16pt \"Bahnschrift\";\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(120, 183, 140);\n"
                                           "    border-radius: 10px;\n"
                                           "    border: 2px solid #000000;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    font: 75 16pt \"Bahnschrift\";\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(100, 183, 140);\n"
                                           "    border-radius: 10px;\n"
                                           "    border: 2px solid #000000;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    font: 75 16pt \"Bahnschrift\";\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(88, 162, 123);\n"
                                           "    border-radius: 10px;\n"
                                           "    border: 2px solid #000000;\n"
                                           "}")
        self.chanhe_password.setObjectName("chanhe_password")
        self.horizontalLayout_9.addWidget(self.chanhe_password, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addWidget(self.change_frame)
        self.save_frame = QtWidgets.QFrame(parent=self.frame)
        self.save_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.save_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.save_frame.setObjectName("save_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.save_frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.save_button = QtWidgets.QPushButton(parent=self.save_frame)
        self.save_button.setMinimumSize(QtCore.QSize(250, 0))
        self.save_button.setMaximumSize(QtCore.QSize(250, 40))
        self.save_button.setStyleSheet("QPushButton {\n"
                                       "    font: 75 16pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 183, 140);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #000000;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    font: 75 16pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(100, 183, 140);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #000000;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    font: 75 16pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(88, 162, 123);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #000000;\n"
                                       "}")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_10.addWidget(self.save_button)
        self.verticalLayout_2.addWidget(self.save_frame)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.name_title.setText(_translate("MainWindow", "Name"))
        self.name_line.setPlaceholderText(_translate("MainWindow", "name"))
        self.surname_title.setText(_translate("MainWindow", "Surname"))
        self.surname_line.setPlaceholderText(_translate("MainWindow", "surname"))
        self.email_title.setText(_translate("MainWindow", "Email"))
        self.email_line.setPlaceholderText(_translate("MainWindow", "email"))
        self.login_title.setText(_translate("MainWindow", "Login"))
        self.login_line.setPlaceholderText(_translate("MainWindow", "login"))
        self.password_title.setText(_translate("MainWindow", "Password"))
        self.password_line.setPlaceholderText(_translate("MainWindow", "password"))
        self.password2_title.setText(_translate("MainWindow", "Password"))
        self.password2_line.setPlaceholderText(_translate("MainWindow", "repeat password"))
        self.chanhe_password.setText(_translate("MainWindow", "Change password"))
        self.save_button.setText(_translate("MainWindow", "Save"))
