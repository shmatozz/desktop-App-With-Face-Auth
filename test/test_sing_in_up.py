import sys
import unittest

from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt

from windows import sign_up_window
from windows import sign_in_window

app = QApplication(sys.argv)


class SignInWindowTest(unittest.TestCase):
    def setUp(self):
        self.form = sign_in_window.SignIn()

    def test_empty_fields(self):
        QTest.mouseClick(self.form.ui.signin_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.helloTitle.text(), "Missing required fields!")

    def test_only_login(self):
        self.form.ui.login.setText("romanda")
        self.form.ui.password.setText("")
        QTest.mouseClick(self.form.ui.signin_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.helloTitle.text(), "Missing required fields!")

    def test_only_password(self):
        self.form.ui.login.setText("")
        self.form.ui.password.setText("123")
        QTest.mouseClick(self.form.ui.signin_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.helloTitle.text(), "Missing required fields!")

    def test_wrong_login(self):
        self.form.ui.login.setText("no_such_login")
        self.form.ui.password.setText("")
        QTest.mouseClick(self.form.ui.signin_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.helloTitle.text(), "Wrong login!")

    def test_wrong_password(self):
        self.form.ui.login.setText("xmatthew")
        self.form.ui.password.setText("wrong_password")
        QTest.mouseClick(self.form.ui.signin_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.helloTitle.text(), "Wrong password!")


class SignUpWindowTest(unittest.TestCase):
    def setUp(self):
        self.form = sign_up_window.SignUp(sign_in_window.SignIn())

    def test_empty_fields(self):
        QTest.mouseClick(self.form.ui.signup_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.RegistrationTitle.text(), "Missing required fields!")

    def test_not_equal_passwords(self):
        self.form.ui.login.setText("test1")
        self.form.ui.name.setText("tester")
        self.form.ui.password.setText("1")
        self.form.ui.passwordRep.setText("11")
        QTest.mouseClick(self.form.ui.signup_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.RegistrationTitle.text(), "Passwords are not equal")

    def test_occupied_login(self):
        self.form.ui.login.setText("xmatthew")
        self.form.ui.name.setText("tester")
        self.form.ui.password.setText("1")
        self.form.ui.passwordRep.setText("1")
        QTest.mouseClick(self.form.ui.signup_button, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.ui.RegistrationTitle.text(), "Login is already occupied")


if __name__ == "__main__":
    unittest.main()
