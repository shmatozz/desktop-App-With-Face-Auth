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
        self.LogPassLayout.setContentsMargins(0, 100, -1, 60)
        self.LogPassLayout.setSpacing(50)
        self.LogPassLayout.setObjectName("LogPassLayout")
        self.helloTitle = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(21)
        self.helloTitle.setFont(font)
        self.helloTitle.setObjectName("helloTitle")
        self.LogPassLayout.addWidget(self.helloTitle, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.login.setMinimumSize(QtCore.QSize(350, 60))
        self.login.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.login.setFont(font)
        self.login.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 15px;                     /* <----  20px  */ \n"
                                 "border: 2px solid #094065;\n"
                                 "padding-left: 20px\n"
                                 "")
        self.login.setMaxLength(20)
        self.login.setClearButtonEnabled(True)
        self.login.setObjectName("login")
        self.LogPassLayout.addWidget(self.login, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
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
                                    "border-radius: 15px;                     /* <----  20px  */ \n"
                                    "border: 2px solid #094065;\n"
                                    "padding-left: 20px\n"
                                    "")
        self.password.setText("")
        self.password.setMaxLength(19)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.LogPassLayout.addWidget(self.password, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
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
        self.SignInButton.setMinimumSize(QtCore.QSize(250, 50))
        self.SignInButton.setMaximumSize(QtCore.QSize(250, 50))
        self.SignInButton.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SignInButton.setFont(font)
        self.SignInButton.setMouseTracking(False)
        self.SignInButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.SignInButton.setAutoFillBackground(False)
        self.SignInButton.setStyleSheet("QPushButton {\n"
                                        "    font: 75 14pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(120, 183, 140);\n"
                                        "    border-radius: 20px;                     /* <----  20px  */ \n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    font: 75 14pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(100, 183, 140);\n"
                                        "    border-radius: 20px;                     /* <----  20px  */ \n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    font: 75 14pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(88, 162, 123);\n"
                                        "    border-radius: 20px;                     /* <----  20px  */ \n"
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
        self.SignUpButton.setMinimumSize(QtCore.QSize(200, 40))
        self.SignUpButton.setMaximumSize(QtCore.QSize(200, 40))
        self.SignUpButton.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setMouseTracking(False)
        self.SignUpButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.SignUpButton.setAutoFillBackground(False)
        self.SignUpButton.setStyleSheet("QPushButton {\n"
                                        "    font: 75 12pt \"Bahnschrift\";\n"
                                        "    color: rgb(120, 183, 140);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-radius: 20px;                     /* <----  20px  */ \n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    font: 75 12pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(100, 183, 140);\n"
                                        "    border-radius: 20px;                     /* <----  20px  */ \n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    font: 75 12pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(88, 162, 123);\n"
                                        "    border-radius: 20px;                     /* <----  20px  */ \n"
                                        "    border: 2px solid #094065;\n"
                                        "}")
        self.SignUpButton.setCheckable(False)
        self.SignUpButton.setAutoDefault(False)
        self.SignUpButton.setObjectName("SignUpButton")
        self.verticalLayout.addWidget(self.SignUpButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.LogPassLayout.addWidget(self.Buttons, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
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
        self.faceAuthNote.setText(_translate("MainWindow",
                                             "You can sign in without password, if you enable face auntification"))
        self.SignInButton.setText(_translate("MainWindow", "Sign In"))
        self.account.setText(_translate("MainWindow", "<html><head/><body><p>Don\'t have account?</p></body></html>"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))
