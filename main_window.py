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

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 154)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.get_date = QtWidgets.QPushButton(self.centralwidget)
        self.get_date.setGeometry(QtCore.QRect(60, 100, 201, 31))
        self.get_date.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.get_date.setObjectName("get_date")
        self.search_text = QtWidgets.QLabel(self.centralwidget)
        self.search_text.setGeometry(QtCore.QRect(120, 10, 151, 21))
        self.search_text.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.search_text.setTextFormat(QtCore.Qt.AutoText)
        self.search_text.setAlignment(QtCore.Qt.AlignCenter)
        self.search_text.setObjectName("search_text")
        self.dataset = QtWidgets.QPushButton(self.centralwidget)
        self.dataset.setGeometry(QtCore.QRect(280, 100, 75, 31))
        self.dataset.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.dataset.setObjectName("dataset")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(50, 40, 321, 51))
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Window"))
        self.get_date.setText(_translate("MainWindow", "Получить данные"))
        self.search_text.setText(_translate("MainWindow", "Выберите дату:"))
        self.dataset.setText(_translate("MainWindow", "Датасет"))

class window_widget(object):
    def setupUi(self, Dialog):
        window_widget.setObjectName("Widget")
        window_widget.resize(219, 190)
        window_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget = QtWidgets.QFrame(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 221, 191))
        self.widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_abel = QtWidgets.QLabel(self.widget)
        self.widget_abel.setTextFormat(QtCore.Qt.AutoText)
        self.widget_abel.setAlignment(QtCore.Qt.AlignCenter)
        self.widget_abel.setObjectName("widget_abel")
        self.verticalLayout.addWidget(self.widget_abel)
        self.widget_actual_dataset_button = QtWidgets.QPushButton(self.widget)
        self.widget_actual_dataset_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.widget_actual_dataset_button.setObjectName("widget_actual_dataset_button")
        self.verticalLayout.addWidget(self.widget_actual_dataset_button)
        self.widget_new_dataset_search = QtWidgets.QLineEdit(self.widget)
        self.widget_new_dataset_search.setStyleSheet("")
        self.widget_new_dataset_search.setText("")
        self.widget_new_dataset_search.setObjectName("widget_new_dataset_search")
        self.verticalLayout.addWidget(self.widget_new_dataset_search)
        self.widget_new_dataset_button = QtWidgets.QPushButton(self.widget)
        self.widget_new_dataset_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.widget_new_dataset_button.setObjectName("widget_new_dataset_button")
        self.verticalLayout.addWidget(self.widget_new_dataset_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.widget_abel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Выберите аннотацию </p><p align=\"center\">датасета, которую </p><p align=\"center\">Вы хотите сохранить</p></body></html>"))
        self.widget_actual_dataset_button.setText(_translate("Dialog", "Исходный датасет"))
        self.widget_new_dataset_button.setText(_translate("Dialog", "Датасет по ссылке"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())