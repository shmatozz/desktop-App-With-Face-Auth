"""
File that implements user interface building of Dialog window.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class UiConfirm(object):
    """
    Build user interface class of Dialog window.

    This class was automatically generated by PyQt.
    """

    def __init__(self):
        # frames
        self.dialog_frame = None
        self.button_frame = None
        # layouts
        self.horizontalLayout = None
        self.horizontalLayout_2 = None
        self.verticalLayout = None
        # buttons
        self.cancel_button = None
        self.ok_button = None
        # labels
        self.question_label = None

    def setupUi(self, Dialog):
        """
        Method that init and place all parts of user interface.

        :param Dialog: window where need to construct interface.
        """
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
        self.dialog_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 20px;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dialog_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_label = QtWidgets.QLabel(parent=self.dialog_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        self.question_label.setFont(font)
        self.question_label.setObjectName("question_label")
        self.verticalLayout.addWidget(self.question_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.button_frame = QtWidgets.QFrame(parent=self.dialog_frame)
        self.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ok_button = QtWidgets.QPushButton(parent=self.button_frame)
        self.ok_button.setMaximumSize(QtCore.QSize(200, 50))
        self.ok_button.setStyleSheet("QPushButton {\n"
                                     "    font: 75 14pt \"Bahnschrift\";\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(120, 183, 140);\n"
                                     "    border-radius: 10px;\n"
                                     "    border: 2px solid #000000;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "    font: 75 14pt \"Bahnschrift\";\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(100, 183, 140);\n"
                                     "    border-radius: 10px;\n"
                                     "    border: 2px solid #000000;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    font: 75 14pt \"Bahnschrift\";\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(88, 162, 123);\n"
                                     "    border-radius: 10px;\n"
                                     "    border: 2px solid #000000;\n"
                                     "}")
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.button_frame)
        self.cancel_button.setMaximumSize(QtCore.QSize(200, 50))
        self.cancel_button.setStyleSheet("QPushButton {\n"
                                         "    font: 75 14pt \"Bahnschrift\";\n"
                                         "    color: rgb(255, 0, 0);\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border-radius: 10px;\n"
                                         "    border: 2px solid #000000;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    font: 75 14pt \"Bahnschrift\";\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color: rgb(234, 0, 0);\n"
                                         "    border-radius: 10px;\n"
                                         "    border: 2px solid #000000;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "    font: 75 14pt \"Bahnschrift\";\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color:rgb(182, 0, 0);\n"
                                         "    border-radius: 10px;\n"
                                         "    border: 2px solid #000000;\n"
                                         "}")
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout.addWidget(self.button_frame)
        self.horizontalLayout.addWidget(self.dialog_frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """
        Method that setup text titles to window and fields.

        :param Dialog: window where need to construct interface.
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.question_label.setText(_translate("Dialog", "Are you sure?"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
