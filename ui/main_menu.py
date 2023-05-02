from PyQt6 import QtCore, QtGui, QtWidgets
from ui import icons_rc


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        icons_rc.qInitResources()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setWindowIcon(QtGui.QIcon("ui/icons/app_icon.ico"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slide_menu_cont = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu_cont.sizePolicy().hasHeightForWidth())
        self.slide_menu_cont.setSizePolicy(sizePolicy)
        self.slide_menu_cont.setMinimumSize(QtCore.QSize(60, 778))
        self.slide_menu_cont.setMaximumSize(QtCore.QSize(60, 778))
        self.slide_menu_cont.setStyleSheet("")
        self.slide_menu_cont.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.slide_menu_cont.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.slide_menu_cont.setObjectName("slide_menu_cont")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slide_menu_cont)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(parent=self.slide_menu_cont)
        self.slide_menu.setMinimumSize(QtCore.QSize(60, 0))
        self.slide_menu.setMaximumSize(QtCore.QSize(60, 976))
        self.slide_menu.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 15px;\n")
        self.slide_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu = QtWidgets.QFrame(parent=self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMinimumSize(QtCore.QSize(30, 0))
        self.menu.setMaximumSize(QtCore.QSize(170, 16777215))
        self.menu.setBaseSize(QtCore.QSize(30, 0))
        self.menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(parent=self.menu)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(10, 3, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button = QtWidgets.QPushButton(parent=self.frame_2)
        self.button.setMinimumSize(QtCore.QSize(40, 40))
        self.button.setMaximumSize(QtCore.QSize(40, 40))
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
        icon.addPixmap(QtGui.QPixmap(":icons/icons/menu.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(30, 30))
        self.button.setObjectName("button")
        self.horizontalLayout_3.addWidget(self.button, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.menu_label = QtWidgets.QLabel(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_label.sizePolicy().hasHeightForWidth())
        self.menu_label.setSizePolicy(sizePolicy)
        self.menu_label.setMaximumSize(QtCore.QSize(0, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        self.menu_label.setFont(font)
        self.menu_label.setObjectName("menu_label")
        self.horizontalLayout_3.addWidget(self.menu_label)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent=self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(170, 0))
        self.frame.setMaximumSize(QtCore.QSize(170, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(10, 15, 0, 0)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.profile = QtWidgets.QPushButton(parent=self.frame)
        self.profile.setMinimumSize(QtCore.QSize(40, 40))
        self.profile.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setKerning(False)
        self.profile.setFont(font)
        self.profile.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":icons/icons/account.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.profile.setIcon(icon1)
        self.profile.setIconSize(QtCore.QSize(30, 30))
        self.profile.setObjectName("profile")
        self.verticalLayout_4.addWidget(self.profile, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.settings = QtWidgets.QPushButton(parent=self.frame)
        self.settings.setMinimumSize(QtCore.QSize(40, 40))
        self.settings.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setKerning(False)
        self.settings.setFont(font)
        self.settings.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.settings.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":icons/icons/settings.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.settings.setIcon(icon2)
        self.settings.setIconSize(QtCore.QSize(30, 30))
        self.settings.setObjectName("settings")
        self.verticalLayout_4.addWidget(self.settings, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.about = QtWidgets.QPushButton(parent=self.frame)
        self.about.setMinimumSize(QtCore.QSize(40, 40))
        self.about.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setKerning(False)
        self.about.setFont(font)
        self.about.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":icons/icons/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.about.setIcon(icon3)
        self.about.setIconSize(QtCore.QSize(30, 30))
        self.about.setObjectName("about")
        self.verticalLayout_4.addWidget(self.about, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.close_menu_button = QtWidgets.QPushButton(parent=self.bottom)
        self.close_menu_button.setMinimumSize(QtCore.QSize(40, 40))
        self.close_menu_button.setMaximumSize(QtCore.QSize(40, 40))
        self.close_menu_button.setStyleSheet("QPushButton {\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":icons/icons/exit_X.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.close_menu_button.setIcon(icon4)
        self.close_menu_button.setIconSize(QtCore.QSize(20, 20))
        self.close_menu_button.setObjectName("close_menu_button")
        self.horizontalLayout_5.addWidget(self.close_menu_button)
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.menu_button)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_2 = QtWidgets.QPushButton(parent=self.menu_button)
        self.button_2.setMinimumSize(QtCore.QSize(0, 40))
        self.button_2.setMaximumSize(QtCore.QSize(0, 40))
        self.button_2.setStyleSheet("QPushButton {\n"
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
        self.button_2.setText("")
        self.button_2.setIcon(icon)
        self.button_2.setIconSize(QtCore.QSize(30, 30))
        self.button_2.setObjectName("button_2")
        self.horizontalLayout_4.addWidget(self.button_2)
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
        self.content.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 15px;\n")
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.image_frame = QtWidgets.QFrame(parent=self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_frame.sizePolicy().hasHeightForWidth())
        self.image_frame.setSizePolicy(sizePolicy)
        self.image_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.image_frame.setObjectName("image_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.image_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.image_output = QtWidgets.QLabel(parent=self.image_frame)
        self.image_output.setText("")
        self.image_output.setObjectName("image_output")
        self.image_output.setMinimumSize(QtCore.QSize(0, 0))
        self.image_output.setMaximumSize(QtCore.QSize(665, 573))
        self.verticalLayout_8.addWidget(self.image_output, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_6.addWidget(self.image_frame)
        self.upload_frame = QtWidgets.QFrame(parent=self.content)
        self.upload_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.upload_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.upload_frame.setObjectName("upload_frame")
        self.upload_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.upload_frame.setMaximumSize(QtCore.QSize(680, 100))
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.upload_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.uploadButton = QtWidgets.QPushButton(parent=self.upload_frame)
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
        self.uploadButton.setObjectName("uploadButton")
        self.verticalLayout_7.addWidget(self.uploadButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.upload_image_label = QtWidgets.QLabel(parent=self.upload_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.upload_image_label.setFont(font)
        self.upload_image_label.setObjectName("upload_image_label")
        self.verticalLayout_7.addWidget(self.upload_image_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_6.addWidget(self.upload_frame)
        self.verticalLayout.addWidget(self.content)
        self.horizontalLayout.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_label.setText(_translate("MainWindow", "  Menu"))
        self.profile.setText(_translate("MainWindow", ""))
        self.settings.setText(_translate("MainWindow", ""))
        self.about.setText(_translate("MainWindow", ""))
        self.close_menu_button.setText(_translate("MainWindow", ""))
        self.hello_title.setText(_translate("MainWindow", "Hello, user!"))
        self.uploadButton.setText(_translate("MainWindow", "Upload"))
        self.upload_image_label.setText(
            _translate("MainWindow", "You can upload image to see how face recognition works"))
