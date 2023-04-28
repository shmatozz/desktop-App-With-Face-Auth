from PyQt6 import QtCore, QtGui, QtWidgets


class UiAbout(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(800, 800)
        About.setMinimumSize(QtCore.QSize(800, 800))
        About.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(parent=About)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.label_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.label_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_frame.setObjectName("label_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.label_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settings_label = QtWidgets.QLabel(parent=self.label_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        self.settings_label.setFont(font)
        self.settings_label.setObjectName("settings_label")
        self.horizontalLayout.addWidget(self.settings_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.label_frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.main = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.github_button = QtWidgets.QPushButton(parent=self.main)
        self.github_button.setMinimumSize(QtCore.QSize(200, 200))
        self.github_button.setMaximumSize(QtCore.QSize(100, 100))
        self.github_button.setBaseSize(QtCore.QSize(100, 0))
        self.github_button.setStyleSheet("QPushButton:pressed{\n"
                                         "    background-color: none;\n"
                                         "    border: 0px\n"
                                         "}")
        self.github_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":icons/icons/github.svg"))
        self.github_button.setIcon(icon)
        self.github_button.setIconSize(QtCore.QSize(170, 170))
        self.github_button.setDefault(False)
        self.github_button.setFlat(True)
        self.github_button.setObjectName("github_button")
        self.horizontalLayout_2.addWidget(self.github_button, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addWidget(self.main)
        self.back_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.back_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.back_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.back_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.back_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.back_frame.setObjectName("back_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.back_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_button = QtWidgets.QPushButton(parent=self.back_frame)
        self.back_button.setEnabled(True)
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
        self.horizontalLayout_3.addWidget(self.back_button)
        self.verticalLayout.addWidget(self.back_frame)
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "MainWindow"))
        self.settings_label.setText(_translate("About", "About"))
        self.back_button.setText(_translate("About", "Back"))
