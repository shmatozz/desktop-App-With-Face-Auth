import unittest

import psycopg2
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt

from windows import connect_to_db

app = QApplication(sys.argv)


class DatabaseTest(unittest.TestCase):

    def test_connection(self):
        try:
            connection = connect_to_db()
            connection.close()
            self.assertEqual(1, 1)
        except psycopg2.Error:
            self.assertEqual(1, 0)

    def test_existing_user(self):
        try:
            connection = connect_to_db()
            with connection.cursor() as cursor:
                cursor.execute(f"select * from users where login = 'xmatthew'")
                info = cursor.fetchall()
                self.assertEqual(len(info), 1)
                self.assertEqual(len(info[0]), 9)
                self.assertEqual(type(info[0][0]), int)
                self.assertEqual(info[0][1], 'Matthew')
                self.assertEqual(info[0][2], 'Baryshev')
                self.assertEqual(info[0][3], 'baryshev.matvey@ya.ru')
                self.assertEqual(info[0][4], 'xmatthew')
                self.assertEqual(info[0][5], '123')
                self.assertEqual(type(info[0][6]), memoryview)
                self.assertEqual(info[0][7], True)
                self.assertEqual(type(info[0][8]), memoryview)
            connection.close()
        except psycopg2.Error:
            self.assertEqual(1, 0)

    def test_non_existing_user(self):
        try:
            connection = connect_to_db()
            with connection.cursor() as cursor:
                cursor.execute(f"select * from users where login = 'no_such_login'")
                info = cursor.fetchall()
                self.assertEqual(len(info), 0)
            connection.close()
        except psycopg2.Error:
            self.assertEqual(1, 0)


if __name__ == '__main__':
    unittest.main()
