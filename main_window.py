import sys
import datetime
import os
import csv
import string

import week
import year
# import functions
import split
import iterator

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def input_date():
    print("input")


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    window.setWindowTitle('Weather')
    window.setGeometry(300, 250, 350, 200)
    
    main_text = QtWidgets.QLabel(window)
    main_text.setText('Set date')
    main_text.move(100, 100)
    main_text.adjustSize()
    
    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("Find")
    btn.setFixedWidth(200)
    btn.clicked.connect(input_date)
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    application()