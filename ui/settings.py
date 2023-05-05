from PyQt6 import QtCore, QtGui, QtWidgets


class UiSettings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.label_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.label_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_frame.setObjectName("label_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.label_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settings_label = QtWidgets.QLabel(parent=self.label_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        self.settings_label.setFont(font)
        self.settings_label.setObjectName("settings_label")
        self.horizontalLayout_2.addWidget(self.settings_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.label_frame)
        self.main_frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.face_auth_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.face_auth_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.face_auth_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.face_auth_frame.setObjectName("face_auth_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.face_auth_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_frame = QtWidgets.QFrame(parent=self.face_auth_frame)
        self.button_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.button_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.face_auth_title = QtWidgets.QLabel(parent=self.button_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.face_auth_title.setFont(font)
        self.face_auth_title.setObjectName("face_auth_title")
        self.horizontalLayout_3.addWidget(self.face_auth_title, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.enable_button = QtWidgets.QRadioButton(parent=self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable_button.sizePolicy().hasHeightForWidth())
        self.enable_button.setSizePolicy(sizePolicy)
        self.enable_button.setMinimumSize(QtCore.QSize(50, 50))
        self.enable_button.setMaximumSize(QtCore.QSize(50, 50))
        self.enable_button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.enable_button.setFont(font)
        self.enable_button.setStyleSheet("QRadioButton::indicator {\n"
                                         "    width: 30px;\n"
                                         "    height: 30px;\n"
                                         "    border-radius: 11px;\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::indicator:checked {\n"
                                         "    background-color: rgb(120, 183, 140);\n"
                                         "    border: 2px solid black;\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton::indicator:unchecked {\n"
                                         "    background-color: white;\n"
                                         "    border:  2px solid black;\n"
                                         "}")
        self.enable_button.setText("")
        self.enable_button.setObjectName("enable_button")
        self.horizontalLayout_3.addWidget(self.enable_button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_4.addWidget(self.button_frame)
        self.upload_frame = QtWidgets.QFrame(parent=self.face_auth_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_frame.sizePolicy().hasHeightForWidth())
        self.upload_frame.setSizePolicy(sizePolicy)
        self.upload_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.upload_frame.setMaximumSize(QtCore.QSize(400, 0))
        self.upload_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.upload_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.upload_frame.setObjectName("upload_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.upload_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.upload_frame)
        self.label.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame = QtWidgets.QFrame(parent=self.upload_frame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uploadButton = QtWidgets.QPushButton(parent=self.frame)
        self.uploadButton.setMinimumSize(QtCore.QSize(200, 40))
        self.uploadButton.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.uploadButton.setFont(font)
        self.uploadButton.setStyleSheet("QPushButton {\n"
                                        "    font: 75 13pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(120, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    font: 75 13pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(100, 183, 140);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    font: 75 13pt \"Bahnschrift\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(88, 162, 123);\n"
                                        "    border-radius: 10px;\n"
                                        "    border: 2px solid #094065;\n"
                                        "}")
        self.uploadButton.setObjectName("uploadButton")
        self.horizontalLayout_4.addWidget(self.uploadButton)
        self.verticalLayout_5.addWidget(self.frame)
        self.verticalLayout_4.addWidget(self.upload_frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.face_auth_frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addWidget(self.main_frame)
        self.back_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.back_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.back_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.back_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.back_frame.setObjectName("back_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.back_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_button = QtWidgets.QPushButton(parent=self.back_frame)
        self.back_button.setMaximumSize(QtCore.QSize(100, 40))
        self.back_button.setStyleSheet("QPushButton {\n"
                                       "    font: 75 14pt \"Bahnschrift\";\n"
                                       "    color: rgb(120, 183, 140);\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #094065;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    font: 75 14pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(100, 183, 140);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #094065;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    font: 75 14pt \"Bahnschrift\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(88, 162, 123);\n"
                                       "    border-radius: 10px;\n"
                                       "    border: 2px solid #094065;\n"
                                       "}")
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)
        self.verticalLayout_2.addWidget(self.back_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settings_label.setText(_translate("MainWindow", "Settings"))
        self.face_auth_title.setText(_translate("MainWindow", "Enable face authentication"))
        self.label.setText(_translate("MainWindow", "You should upload a photo that clearly shows your face.\n"
                                                    "This photo will be used to determine the match at the sign in."))
        self.uploadButton.setText(_translate("MainWindow", "Upload"))
        self.back_button.setText(_translate("MainWindow", "Back"))
