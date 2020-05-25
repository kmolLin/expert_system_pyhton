# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'animal.py'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from ui_animal import Ui_Animals
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
import os


def IsEvidence(x):
    for i in mywindow.fact:
        if x == i[-2]:
            return False
    return True


def getData(x):
    data = []
    for i in mywindow.fact:
        tr = []
        if x == i[-2]:
            for j in range(0, len(i) - 1):
                tr.append(i[j])
            data.append(tr)
    return data


class mywindow(QWidget, Ui_Animals):
    fact = []
    conditions = set("")
    res = set("")

    def __init__(self):
        super(mywindow, self).__init__()
        f = open("rules.txt", "r", encoding="utf-8")
        for line in f:
            ls = line.strip('\n').split(" ")
            mywindow.fact.append(ls)
        f.close()
        self.texx = None
        for i in mywindow.fact:
            for j in range(0, len(i) - 2):
                mywindow.conditions.add(i[j])
            mywindow.res.add(i[-2])
        self.setupUi(self)

    def backs(self, data):
        c = 0
        flag = False
        for i in data:
            d = "if "
            for s in range(0, len(i)):
                if s == len(i) - 2:
                    d = d + str(i[s]) + " then "
                else:
                    d = d + str(i[s]) + " "
            window.TL.append(d)
            for j in range(0, len(i) - 1):
                if IsEvidence(i[j]):
                    a = QMessageBox.question(self, '提示', f"{i[j]}嗎",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    print(i[j] + "嗎?")
                    # r = input()
                    # print(a)
                    if a == QMessageBox.Yes:
                        c = c + 1
                else:
                    temp = getData(i[j])
                    if self.backs(temp):
                        c = c + 1
            if c >= i.__len__() - 1:
                flag = True
                print(i[-1])
                print("驗證成功")
                break
            elif 0 < c < (i.__len__() - 1):
                flag = True
                print(i[-1])
                self.texx = "可能接近"
                print("可能接近")
                print(c, i.__len__() - 1)
                self.showlabel.setText(f"可能接近 {c / (i.__len__() - 1)}")
                break
            else:
                flag = False
                print(i[-1])
                print("驗證失敗")
        if flag:
            return True
        else:
            return False

    def resizeEvent(self, event):
        palette = QPalette()
        # pix = QtGui.QPixmap('images/3.jpg')
        # pix = pix.scaled(self.width(), self.height())
        # palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        # self.setPalette(palette)

    def test(self):
        if self.checkBox.isChecked():  # 逆向推理
            i = self.comboBox.currentIndex()
            s = self.comboBox.itemText(i)
            print(s)
            data = getData(s)
            print(data)
            if self.backs(data):
                if self.texx:
                    QMessageBox.information(self, "提示", f"該動物可能是{data[0][-1]}", QMessageBox.Yes)
                    self.result.setText("專家系統分析該動物可能是" + data[0][-1])
                else:
                    QMessageBox.information(self, "提示", f"該動物是{data[0][-1]}", QMessageBox.Yes)
                    self.result.setText("專家系統分析該動物是" + data[0][-1])
            else:
                self.result.setText("專家分析該動物不是" + data[0][-1])
                a = QMessageBox.information(self, "提示", f"該動物不是{data[0][-1]}", QMessageBox.Yes)
        else:  # 正向推理
            s = self.input.toPlainText()
            tl = ""
            description = s.split("\n")
            print("des")
            print(description)
            line = 0
            for i in mywindow.fact:
                same = 0
                for j in range(0, len(i)):
                    if j >= len(i) - 2:
                        break
                    for k in range(0, len(description)):
                        if i[j] == description[k]:
                            same = same + 1
                            break
                    if k == len(description):
                        break

                if same == i.__len__() - 2:
                    print("same=i")
                    line = 1
                    if i[-1] == "*":  # 是结论
                        d = "if "
                        for s in range(0, len(i) - 1):
                            if s == len(i) - 3:
                                d = d + str(i[s]) + " then "
                            else:
                                d = d + str(i[s]) + " "
                        tl = tl + d + "\n"
                        self.TL.setText(tl)
                        self.result.setText("專家系統分析該動物是" + i[-2])
                        print(i[-2])
                    else:
                        line = 1
                        d = "if "
                        for s in range(0, len(i) - 1):
                            if s == len(i) - 3:
                                d = d + str(i[s]) + " then "
                            else:
                                d = d + str(i[s]) + " "
                        tl = tl + d + "\n"
                        self.TL.setText(tl)
                        self.result.setText("專家也不知道具體是什麽動物，大概率推測是" + i[-2])
                        description.append(i[-2])
            if line == 0:
                self.result.setText("專家也不知道具體是什麽動物")

    def selectInit(self):
        mywindow.fact.clear()
        mywindow.conditions.clear()
        mywindow.res.clear()
        f = open("rules.txt", "r", encoding="utf-8")
        for line in f:
            ls = line.strip('\n').split(" ")
            mywindow.fact.append(ls)
        f.close()
        for i in mywindow.fact:
            for j in range(0, len(i) - 2):
                mywindow.conditions.add(i[j])
            mywindow.res.add(i[-2])
        self.comboBox.clear()
        self.input.clear()
        self.result.clear()
        self.TL.clear()
        if self.checkBox.isChecked():
            for x in mywindow.res:
                self.comboBox.addItem(str(x))
        else:
            for x in mywindow.conditions:
                self.comboBox.addItem(str(x))

    def selectChange(self):
        if self.checkBox.isChecked():
            self.input.clear()
            i = self.comboBox.currentIndex()
            s = self.comboBox.itemText(i)
            self.input.append(s)
        else:
            i = self.comboBox.currentIndex()
            s = self.comboBox.itemText(i)
            self.input.append(s)

    def checkChange(self):
        self.comboBox.clear()
        if self.checkBox.isChecked():
            for x in mywindow.res:
                self.comboBox.addItem(str(x))
        else:
            for x in mywindow.conditions:
                self.comboBox.addItem(str(x))

    def rules(self):
        os.startfile('rules.txt')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
