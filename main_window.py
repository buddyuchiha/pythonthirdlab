import sys
import datetime
import os
import csv
import string

import week
import year
from functions import get_info
import split
import iterator

from os import path
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow
from design import Ui_MainWindow


class Weather(QMainWindow):
    def __init__(self):
        super(Weather, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_chose_file.clicked.connect(self.get_file_path)
        self.ui.get_folder_split_csv_x_y.clicked.connect(self.get_file_path)
        self.ui.get_folder_button_split_csv_year.clicked.connect(self.get_file_path)
        self.ui.get_folder_button_split_csv_weeks.clicked.connect(self.get_file_path)
        self.ui.button_weather.clicked.connect(self.get_weather_info)
        # self.get_data_button.clicked.connect(self.get_file_date)
        chose_file_path = ""
        chose_x_y__path = ""
        chose_years_path = ""
        chose_weaks_path = ""
        iter = ""
        
        
    def get_file_path(self):
        try:
            self.chose_file_path = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'Выберите папку')
            QtWidgets.QMessageBox.information(
                self, 'Папка выбрана', self.chose_file_path)
            self.chose_file_path += "/dataset.csv"
        except:
            QtWidgets.QMessageBox.information(
            self, 'Ошибка', 'Выбран невозможный датасет')
        
    def get_weather_info(self):
        try:
            selected_date = self.ui.button_chose_weather.date().toString("yyyy-MM-dd")
            print(selected_date)
            info = get_info(selected_date, self.chose_file_path)
            QtWidgets.QMessageBox.information(
            self, 'Данные за этот год', info)
        except:
            QtWidgets.QMessageBox.information(
            self, 'Ошибка', 'Вы не выбрали датасет')

         
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Weather()
    window.show()
    sys.exit(app.exec())