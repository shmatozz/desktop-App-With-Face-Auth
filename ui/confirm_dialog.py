from PyQt6 import QtCore, QtGui, QtWidgets


class UiConfirm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Dialog.resize(300, 150)
        Dialog.setMinimumSize(QtCore.QSize(300, 150))
        Dialog.setMaximumSize(QtCore.QSize(300, 150))
        Dialog.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-radius: 20px;\n")
        Dialog.setSizeGripEnabled(False)
        Dialog.setWindowIcon(QtGui.QIcon(":/icons/icons/chat.png"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dialog_frame = QtWidgets.QFrame(parent=Dialog)
        self.dialog_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dialog_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dialog_frame.setObjectName("dialog_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dialog_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_laber = QtWidgets.QLabel(parent=self.dialog_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        self.question_laber.setFont(font)
        self.question_laber.setObjectName("question_label")
        self.verticalLayout.addWidget(self.question_laber, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(parent=self.dialog_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ok_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.ok_button.setMaximumSize(QtCore.QSize(200, 50))
        self.ok_button.setStyleSheet("QPushButton {\n"
                                     "    font: 75 14pt \"Bahnschrift\";\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(120, 183, 140);\n"
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
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.cancel_button.setMaximumSize(QtCore.QSize(200, 50))
        self.cancel_button.setStyleSheet("QPushButton {\n"
                                         "    font: 75 14pt \"Bahnschrift\";\n"
                                         "    color: rgb(255, 0, 0);\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border-radius: 10px;                     /* <----  20px  */ \n"
                                         "    border: 2px solid #094065;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    font: 75 14pt \"Bahnschrift\";\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color: rgb(234, 0, 0);\n"
                                         "    border-radius: 10px;                     /* <----  20px  */ \n"
                                         "    border: 2px solid #094065;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "    font: 75 14pt \"Bahnschrift\";\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color:rgb(182, 0, 0);\n"
                                         "    border-radius: 10px;                     /* <----  20px  */ \n"
                                         "    border: 2px solid #094065;\n"
                                         "}")
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.dialog_frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.question_laber.setText(_translate("Dialog", "Are you sure?"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
