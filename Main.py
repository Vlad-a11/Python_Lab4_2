#!/usr/bin/env python3
# coding=utf-8

import re
import sys
import random
import string

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn2.clicked.connect(self.solve2)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        txt=text.split()
        for s in txt:

            self.textEdit_words.insertPlainText(s[::2]+"\n")

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()




    def solve2(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        for i in text:
            self.textEdit_words.insertPlainText(i + random.choice(string.ascii_letters))
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
