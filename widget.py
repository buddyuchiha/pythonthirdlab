# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(219, 190)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
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
