# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file '動物識別專家系統.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
class Ui_Animals(object):
    def setupUi(self, Animals):
        Animals.setObjectName("Animals")
        Animals.resize(1127, 710)
        Animals.setAutoFillBackground(True)
        self.TL = QtWidgets.QTextEdit(Animals)
        self.TL.setGeometry(QtCore.QRect(670, 200, 251, 211))
        self.TL.setObjectName("TL")
        self.input = QtWidgets.QTextEdit(Animals)
        self.input.setGeometry(QtCore.QRect(240, 100, 151, 321))
        self.input.setAutoFillBackground(False)
        self.input.setObjectName("input")
        self.result = QtWidgets.QTextEdit(Animals)
        self.result.setGeometry(QtCore.QRect(670, 100, 251, 51))
        self.result.setObjectName("result")
        self.result.setReadOnly(True)
        self.input_lable = QtWidgets.QLabel(Animals)
        self.input_lable.setGeometry(QtCore.QRect(100, 80, 141, 41))
        self.input_lable.setObjectName("input_lable")
        self.input_lable.setFont(QFont("Roman times", 10, QFont.Bold))
        self.TL_label = QtWidgets.QLabel(Animals)
        self.TL_label.setGeometry(QtCore.QRect(750, 150, 101, 61))
        self.TL_label.setObjectName("TL_label")
        self.TL_label.setFont(QFont("Roman times", 10, QFont.Bold))
        self.result_label = QtWidgets.QLabel(Animals)
        self.result_label.setGeometry(QtCore.QRect(750, 70, 111, 31))
        self.result_label.setObjectName("result_label")
        self.result_label.setFont(QFont("Roman times", 10, QFont.Bold))
        self.scrollArea = QtWidgets.QScrollArea(Animals)
        self.scrollArea.setGeometry(QtCore.QRect(90, 120, 141, 20))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 139, 18))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 141, 21))
        self.comboBox.setObjectName("comboBox")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(Animals)
        self.pushButton.setGeometry(QtCore.QRect(500, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(QFont("Roman times", 10, QFont.Bold))
        self.checkBox = QtWidgets.QCheckBox(Animals)
        self.checkBox.setGeometry(QtCore.QRect(500, 190, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setFont(QFont("Roman times", 10, QFont.Bold))
        self.pushButton_2 = QtWidgets.QPushButton(Animals)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(QFont("Roman times", 10, QFont.Bold))
        self.pushButton_3 = QtWidgets.QPushButton(Animals)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 300, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(QFont("Roman times", 10, QFont.Bold))
        self.retranslateUi(Animals)
        self.pushButton.clicked.connect(Animals.test)
        self.comboBox.activated['int'].connect(Animals.selectChange)
        self.checkBox.stateChanged['int'].connect(Animals.checkChange)
        self.pushButton_2.clicked.connect(Animals.selectInit)
        self.pushButton_3.clicked.connect(Animals.rules)
        QtCore.QMetaObject.connectSlotsByName(Animals)
    def retranslateUi(self, Animals):
        _translate = QtCore.QCoreApplication.translate
        Animals.setWindowTitle(_translate("Animals", "Form"))
        self.input_lable.setText(_translate("Animals", "請輸入已知事實"))
        self.TL_label.setText(_translate("Animals", "推理過程"))
        self.result_label.setText(_translate("Animals", "專家分析結果"))
        self.pushButton.setText(_translate("Animals", "推理"))
        self.checkBox.setText(_translate("Animals", "反向推理"))
        self.pushButton_2.setText(_translate("Animals", "初始化"))
        self.pushButton_3.setText(_translate("Animals", "修改規則庫"))