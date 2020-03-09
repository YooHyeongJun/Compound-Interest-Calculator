# -*- coding: utf-8 -*-
day = 0
percent = 0
money = 0

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("복리계산기")
        self.setWindowIcon(QIcon('money.png'))
        self.setFixedSize(500, 400)

        days_label = QLabel("날짜 : ", self)
        days_label.move(60, 50)

        percent_label = QLabel("퍼센트 : ", self)
        percent_label.move(60, 140)

        money_label = QLabel("처음돈 : ", self)
        money_label.move(60, 230)

        self.label = QLabel("", self)
        self.label.move(50, 300)
        self.label.resize(500, 30)

        self.lineEdit1 = QLineEdit("", self)
        self.lineEdit1.move(110, 50)
        self.lineEdit1.textChanged.connect(self.lineEditChanged1)

        self.lineEdit2 = QLineEdit("", self)
        self.lineEdit2.move(110, 140)
        self.lineEdit2.textChanged.connect(self.lineEditChanged2)

        self.lineEdit3 = QLineEdit("", self)
        self.lineEdit3.move(110, 230)
        self.lineEdit3.textChanged.connect(self.lineEditChanged3)

        self.btn1 = QPushButton("계산", self)
        self.btn1.move(350, 230)
        self.btn1.clicked.connect(self.calculate)

        self.maker = QLabel("제작자 : 유형준", self)
        self.maker.move(10, 360)
        self.maker.resize(200, 50)


    def lineEditChanged1(self):
        global day
        day = self.lineEdit1.text()

    def lineEditChanged2(self):
        global percent
        percent = self.lineEdit2.text()

    def lineEditChanged3(self):
        global money
        money = self.lineEdit3.text()

    def calculate(self):
        global day, percent, money
        days = int(day)
        percents = int(percent)
        moneys = int(money)

        for i in range(days):
            moneys += moneys * (0.01) * percents

        self.label.setText("{}일동안 하루 {}퍼센트의 복리 결과는 {}원입니다.".format(days, percents, int(moneys)))

if __name__ == "__main__":
    num_list = []
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()