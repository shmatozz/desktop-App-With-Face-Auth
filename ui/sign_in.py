from PyQt6 import QtCore, QtGui, QtWidgets


class UiSignIn(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        MainWindow.setMaximumSize(QtCore.QSize(500, 700))
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LogPassLayout = QtWidgets.QVBoxLayout()
        self.LogPassLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.LogPassLayout.setContentsMargins(0, 50, -1, 60)
        self.LogPassLayout.setSpacing(0)
        self.LogPassLayout.setObjectName("LogPassLayout")
        self.helloTitle = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(21)
        self.helloTitle.setFont(font)
        self.helloTitle.setObjectName("helloTitle")
        self.LogPassLayout.addWidget(self.helloTitle, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.log_pass_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.log_pass_frame.setMinimumSize(QtCore.QSize(0, 250))
        self.log_pass_frame.setMaximumSize(QtCore.QSize(16777215, 400))
        self.log_pass_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.log_pass_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.log_pass_frame.setObjectName("log_pass_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.log_pass_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.login = QtWidgets.QLineEdit(parent=self.log_pass_frame)
        self.login.setMinimumSize(QtCore.QSize(350, 60))
        self.login.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.login.setFont(font)
        self.login.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 10px;\n"
                                 "border: 2px solid #000000;\n"
                                 "padding-left: 20px")
        self.login.setMaxLength(20)
        self.login.setClearButtonEnabled(True)
        self.login.setObjectName("login")
        self.verticalLayout_2.addWidget(self.login, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.password = QtWidgets.QLineEdit(parent=self.log_pass_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QtCore.QSize(350, 60))
        self.password.setMaximumSize(QtCore.QSize(350, 60))
        self.password.setBaseSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;\n"
                                    "border: 2px solid #000000;\n"
                                    "padding-left: 20px")
        self.password.setText("")
        self.password.setMaxLength(19)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.remember_me_check = QtWidgets.QCheckBox(parent=self.log_pass_frame)
        self.remember_me_check.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.remember_me_check.setFont(font)
        self.remember_me_check.setObjectName("remember_me_check")
        self.verticalLayout_2.addWidget(self.remember_me_check, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.LogPassLayout.addWidget(self.log_pass_frame)
        self.Buttons = QtWidgets.QFrame(parent=self.centralwidget)
        self.Buttons.setMinimumSize(QtCore.QSize(400, 200))
        self.Buttons.setMaximumSize(QtCore.QSize(255, 170))
        self.Buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Buttons.setObjectName("Buttons")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Buttons)
        self.verticalLayout.setObjectName("verticalLayout")
        self.faceAuthNote = QtWidgets.QLabel(parent=self.Buttons)
        self.faceAuthNote.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        self.faceAuthNote.setFont(font)
        self.faceAuthNote.setObjectName("faceAuthNote")
        self.verticalLayout.addWidget(self.faceAuthNote, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.SignInButton = QtWidgets.QPushButton(parent=self.Buttons)
        self.SignInButton.setEnabled(True)
        self.SignInButton.setMinimumSize(QtCore.QSize(200, 50))
        self.SignInButton.setMaximumSize(QtCore.QSize(200, 50))
        self.SignInButton.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SignInButton.setFont(font)
        self.SignInButton.setMouseTracking(False)
        self.SignInButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.SignInButton.setAutoFillBackground(False)
        self.SignInButton.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(120, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(100, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(88, 162, 123);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}")
        self.SignInButton.setCheckable(False)
        self.SignInButton.setAutoDefault(False)
        self.SignInButton.setObjectName("SignInButton")
        self.verticalLayout.addWidget(self.SignInButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.account = QtWidgets.QLabel(parent=self.Buttons)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.account.setFont(font)
        self.account.setObjectName("account")
        self.verticalLayout.addWidget(self.account, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.SignUpButton = QtWidgets.QPushButton(parent=self.Buttons)
        self.SignUpButton.setEnabled(True)
        self.SignUpButton.setMinimumSize(QtCore.QSize(150, 40))
        self.SignUpButton.setMaximumSize(QtCore.QSize(150, 40))
        self.SignUpButton.setBaseSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setMouseTracking(False)
        self.SignUpButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.SignUpButton.setAutoFillBackground(False)
        self.SignUpButton.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(120, 183, 140);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(100, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(88, 162, 123);\n"
                                        "    border-radius: 10px; \n"
                                        "    border: 2px solid #094065;\n"
                                        "}")
        self.SignUpButton.setCheckable(False)
        self.SignUpButton.setAutoDefault(False)
        self.SignUpButton.setObjectName("SignUpButton")
        self.verticalLayout.addWidget(self.SignUpButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.LogPassLayout.addWidget(self.Buttons, 0,
                                     QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_3.addLayout(self.LogPassLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.helloTitle.setText(_translate("MainWindow", "Hello!"))
        self.login.setPlaceholderText(_translate("MainWindow", "login"))
        self.password.setPlaceholderText(_translate("MainWindow", "password"))
        self.remember_me_check.setText(_translate("MainWindow", "Remember me"))
        self.faceAuthNote.setText(_translate("MainWindow",
                                             "<html><head/><body><p>You can sign in without password, if you enable face auntification</p></body></html>"))
        self.SignInButton.setText(_translate("MainWindow", "Sign In"))
        self.account.setText(_translate("MainWindow", "<html><head/><body><p>Don\'t have account?</p></body></html>"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))