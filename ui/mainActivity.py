from PyQt6 import QtCore, QtGui, QtWidgets
from ui import icons_rc


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 822)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 822))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slide_menu_cont = QtWidgets.QFrame(parent=self.centralwidget)
        self.slide_menu_cont.setMinimumSize(QtCore.QSize(200, 800))
        self.slide_menu_cont.setMaximumSize(QtCore.QSize(200, 800))
        self.slide_menu_cont.setStyleSheet("")
        self.slide_menu_cont.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.slide_menu_cont.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.slide_menu_cont.setObjectName("slide_menu_cont")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slide_menu_cont)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(parent=self.slide_menu_cont)
        self.slide_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.slide_menu.setMaximumSize(QtCore.QSize(220, 976))
        self.slide_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu = QtWidgets.QFrame(parent=self.slide_menu)
        self.menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.menu_label = QtWidgets.QLabel(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_label.sizePolicy().hasHeightForWidth())
        self.menu_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        self.menu_label.setFont(font)
        self.menu_label.setObjectName("menu_label")
        self.verticalLayout_5.addWidget(self.menu_label, 0,
                                        QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame = QtWidgets.QFrame(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.profile = QtWidgets.QPushButton(parent=self.frame)
        self.profile.setMinimumSize(QtCore.QSize(0, 50))
        self.profile.setStyleSheet("QPushButton {\n"
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
        self.profile.setObjectName("profile")
        self.verticalLayout_4.addWidget(self.profile)
        self.settings = QtWidgets.QPushButton(parent=self.frame)
        self.settings.setMinimumSize(QtCore.QSize(0, 50))
        self.settings.setStyleSheet("QPushButton {\n"
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
        self.settings.setObjectName("settings")
        self.verticalLayout_4.addWidget(self.settings)
        self.about = QtWidgets.QPushButton(parent=self.frame)
        self.about.setMinimumSize(QtCore.QSize(0, 50))
        self.about.setStyleSheet("QPushButton {\n"
                                 "    font: 75 14pt \"Bahnschrift\";\n"
                                 "    color: rgb(120, 183, 140);\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "    border-radius: 20px;                     /* <----  20px  */ \n"
                                 "    border: 2px solid #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover{\n"
                                 "    font: 75 14pt \"Bahnschrift\";\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(100, 183, 140);\n"
                                 "    border-radius: 20px;                     /* <----  20px  */ \n"
                                 "    border: 2px solid #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    font: 75 14pt \"Bahnschrift\";\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(88, 162, 123);\n"
                                 "    border-radius: 20px;                     /* <----  20px  */ \n"
                                 "    border: 2px solid #000000;\n"
                                 "}")
        self.about.setObjectName("about")
        self.verticalLayout_4.addWidget(self.about)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.menu)
        self.bottom = QtWidgets.QFrame(parent=self.slide_menu)
        self.bottom.setMinimumSize(QtCore.QSize(0, 50))
        self.bottom.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_3.addWidget(self.bottom)
        self.verticalLayout_2.addWidget(self.slide_menu)
        self.horizontalLayout.addWidget(self.slide_menu_cont)
        self.main = QtWidgets.QFrame(parent=self.centralwidget)
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(parent=self.main)
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_button = QtWidgets.QFrame(parent=self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy)
        self.menu_button.setMinimumSize(QtCore.QSize(50, 50))
        self.menu_button.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menu_button.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_button.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_button.setObjectName("menu_button")
        self.button = QtWidgets.QPushButton(parent=self.menu_button)
        self.button.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.button.setMinimumSize(QtCore.QSize(50, 50))
        self.button.setMaximumSize(QtCore.QSize(50, 50))
        self.button.setStyleSheet("QPushButton {\n"
                                  "    font: 75 14pt \"Bahnschrift\";\n"
                                  "    color: rgb(120, 183, 140);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "    border-radius: 20px;                     /* <----  20px  */ \n"
                                  "    border: 2px solid #000000;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "    font: 75 14pt \"Bahnschrift\";\n"
                                  "    color: rgb(120, 183, 140);\n"
                                  "    background-color: rgb(239, 239, 239);\n"
                                  "    border-radius: 20px;                     /* <----  20px  */ \n"
                                  "    border: 2px solid #000000;\n"
                                  "}")
        self.button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setObjectName("button")
        self.horizontalLayout_2.addWidget(self.menu_button, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.hello_title = QtWidgets.QLabel(parent=self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hello_title.sizePolicy().hasHeightForWidth())
        self.hello_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        self.hello_title.setFont(font)
        self.hello_title.setObjectName("hello_title")
        self.horizontalLayout_2.addWidget(self.hello_title, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.empty_frame = QtWidgets.QFrame(parent=self.header)
        self.empty_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.empty_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.empty_frame.setObjectName("empty_frame")
        self.horizontalLayout_2.addWidget(self.empty_frame)
        self.verticalLayout.addWidget(self.header)
        self.content = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.verticalLayout.addWidget(self.content)
        self.horizontalLayout.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_label.setText(_translate("MainWindow", "Menu"))
        self.profile.setText(_translate("MainWindow", "Profile"))
        self.settings.setText(_translate("MainWindow", "Settings"))
        self.about.setText(_translate("MainWindow", "About"))
        self.hello_title.setText(_translate("MainWindow", "Hello, user!"))
