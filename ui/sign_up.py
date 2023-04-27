from PyQt6 import QtCore, QtGui, QtWidgets


class UiSignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        MainWindow.setMaximumSize(QtCore.QSize(500, 700))
        MainWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 500, 700))
        self.scrollArea.setMinimumSize(QtCore.QSize(500, 700))
        self.scrollArea.setMaximumSize(QtCore.QSize(500, 700))
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
                                      "    border: none;\n"
                                      "    background: rgb(229, 229, 229);\n"
                                      "    width: 10px;\n"
                                      "    margin: 10px 0 10px 0;\n"
                                      "    border-radius: 0px;\n"
                                      " }\n"
                                      "\n"
                                      "/*  HANDLE BAR VERTICAL */\n"
                                      "QScrollBar::handle:vertical {    \n"
                                      "    background-color: rgb(229, 229, 229);\n"
                                      "    min-height: 30px;\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:hover{    \n"
                                      "    background-color: rgb(229, 229, 229);\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:pressed {    \n"
                                      "    background-color: rgb(229, 229, 229);\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN TOP - SCROLLBAR */\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color:rgb(120, 183, 140);\n"
                                      "    height: 0px;\n"
                                      "    border-top-left-radius: 0px;\n"
                                      "    border-top-right-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:hover {    \n"
                                      "    background-color: rgb(255, 0, 127);\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:pressed {    \n"
                                      "    background-color: rgb(185, 0, 92);\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN BOTTOM - SCROLLBAR */\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color: rgb(120, 183, 140);\n"
                                      "    height: 0px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:hover {    \n"
                                      "    background-color: rgb(255, 0, 127);\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:pressed {    \n"
                                      "    background-color: rgb(185, 0, 92);\n"
                                      "}\n"
                                      "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -324, 488, 1022))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1000))
        self.frame.setMaximumSize(QtCore.QSize(500, 1000))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RegistrationTitle = QtWidgets.QLabel(parent=self.frame)
        self.RegistrationTitle.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(21)
        self.RegistrationTitle.setFont(font)
        self.RegistrationTitle.setObjectName("RegistrationTitle")
        self.verticalLayout_2.addWidget(self.RegistrationTitle, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.name = QtWidgets.QLineEdit(parent=self.frame)
        self.name.setMinimumSize(QtCore.QSize(350, 60))
        self.name.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "border-radius: 10px;\n"
                                "border: 2px solid #000000;\n"
                                "padding-left: 20px\n"
                                "")
        self.name.setText("")
        self.name.setMaxLength(20)
        self.name.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.name.setClearButtonEnabled(True)
        self.name.setObjectName("name")
        self.verticalLayout_2.addWidget(self.name, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.surname = QtWidgets.QLineEdit(parent=self.frame)
        self.surname.setMinimumSize(QtCore.QSize(350, 60))
        self.surname.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.surname.setFont(font)
        self.surname.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 10px;\n"
                                   "border: 2px solid #000000;\n"
                                   "padding-left: 20px\n"
                                   "")
        self.surname.setMaxLength(20)
        self.surname.setClearButtonEnabled(True)
        self.surname.setObjectName("surname")
        self.verticalLayout_2.addWidget(self.surname, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.email = QtWidgets.QLineEdit(parent=self.frame)
        self.email.setMinimumSize(QtCore.QSize(350, 60))
        self.email.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.email.setFont(font)
        self.email.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 10px;\n"
                                 "border: 2px solid #000000;\n"
                                 "padding-left: 20px\n"
                                 "")
        self.email.setMaxLength(20)
        self.email.setClearButtonEnabled(True)
        self.email.setObjectName("email")
        self.verticalLayout_2.addWidget(self.email, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.login = QtWidgets.QLineEdit(parent=self.frame)
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
                                 "padding-left: 20px\n"
                                 "")
        self.login.setMaxLength(20)
        self.login.setClearButtonEnabled(True)
        self.login.setObjectName("login")
        self.verticalLayout_2.addWidget(self.login, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.password = QtWidgets.QLineEdit(parent=self.frame)
        self.password.setMinimumSize(QtCore.QSize(350, 60))
        self.password.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;\n"
                                    "border: 2px solid #000000;\n"
                                    "padding-left: 20px\n"
                                    "")
        self.password.setMaxLength(20)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.passwordRep = QtWidgets.QLineEdit(parent=self.frame)
        self.passwordRep.setMinimumSize(QtCore.QSize(350, 60))
        self.passwordRep.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.passwordRep.setFont(font)
        self.passwordRep.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;\n"
                                       "border: 2px solid #000000;\n"
                                       "padding-left: 20px\n"
                                       "")
        self.passwordRep.setMaxLength(20)
        self.passwordRep.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordRep.setClearButtonEnabled(True)
        self.passwordRep.setObjectName("passwordRep")
        self.verticalLayout_2.addWidget(self.passwordRep, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.uploadLayout = QtWidgets.QVBoxLayout()
        self.uploadLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.uploadLayout.setSpacing(0)
        self.uploadLayout.setObjectName("uploadLayout")
        self.uploadMes = QtWidgets.QLabel(parent=self.frame)
        self.uploadMes.setEnabled(False)
        self.uploadMes.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        self.uploadMes.setFont(font)
        self.uploadMes.setObjectName("uploadMes")
        self.uploadLayout.addWidget(self.uploadMes, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.uploadButton = QtWidgets.QPushButton(parent=self.frame)
        self.uploadButton.setMinimumSize(QtCore.QSize(150, 0))
        self.uploadButton.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.uploadButton.setFont(font)
        self.uploadButton.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(120, 183, 140);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #000000;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(100, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #000000;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(88, 162, 123);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #000000;\n"
                                        "}")
        self.uploadButton.setObjectName("uploadButton")
        self.uploadLayout.addWidget(self.uploadButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addLayout(self.uploadLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.SingUpButton = QtWidgets.QPushButton(parent=self.frame)
        self.SingUpButton.setEnabled(True)
        self.SingUpButton.setMinimumSize(QtCore.QSize(200, 50))
        self.SingUpButton.setMaximumSize(QtCore.QSize(200, 50))
        self.SingUpButton.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SingUpButton.setFont(font)
        self.SingUpButton.setMouseTracking(False)
        self.SingUpButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.SingUpButton.setAutoFillBackground(False)
        self.SingUpButton.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(120, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #000000;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(100, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #000000;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(88, 162, 123);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #000000;\n"
                                        "}")
        self.SingUpButton.setCheckable(False)
        self.SingUpButton.setAutoDefault(False)
        self.SingUpButton.setObjectName("SingUpButton")
        self.verticalLayout_2.addWidget(self.SingUpButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.backButton = QtWidgets.QPushButton(parent=self.frame)
        self.backButton.setMinimumSize(QtCore.QSize(80, 0))
        self.backButton.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(120, 183, 140);\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "    border: 2px solid #000000;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(100, 183, 140);\n"
                                      "    border-radius: 10px;\n"
                                      "    border: 2px solid #000000;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(88, 162, 123);\n"
                                      "    border-radius: 10px;\n"
                                      "    border: 2px solid #000000;\n"
                                      "}")
        self.backButton.setObjectName("backButton")
        self.verticalLayout_2.addWidget(self.backButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RegistrationTitle.setText(_translate("MainWindow", "Registration"))
        self.name.setPlaceholderText(_translate("MainWindow", "> name"))
        self.surname.setPlaceholderText(_translate("MainWindow", "surname"))
        self.email.setPlaceholderText(_translate("MainWindow", "email"))
        self.login.setPlaceholderText(_translate("MainWindow", "> login"))
        self.password.setPlaceholderText(_translate("MainWindow", "> password"))
        self.passwordRep.setPlaceholderText(_translate("MainWindow", "> repeat password"))
        self.uploadMes.setText(_translate("MainWindow",
                                          "<html><head/><body><p>Upload photo with your face for face authentication</p></body></html>"))
        self.uploadButton.setText(_translate("MainWindow", "Upload"))
        self.SingUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.backButton.setText(_translate("MainWindow", "Back"))