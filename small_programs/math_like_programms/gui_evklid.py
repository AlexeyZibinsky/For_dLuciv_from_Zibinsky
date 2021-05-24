import sys
from PyQt5.QtWidgets import * # Удобно
from PyQt5.QtCore import *
from PyQt5 import QtWidgets


def algoritm_Evklida(a, b):
    a, b = abs(a), abs(b)
    while True:
        if a > b:
            a -= b
        elif b > a:
            b -= a
        else:
            return a


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("EUCLID'S ALGORITHM") # Заголовок вверху окна
        self.setGeometry(300, 300, 500, 100) # Положение окна на экране и размеры
        self.line_edit = QLineEdit(self) # Создаём поле ввода
        self.line_edit.setGeometry(0, 0, 500, 33)
        self.line_edit_2 = QLineEdit(self)
        self.line_edit_2.setGeometry(0, 33, 500, 33)
        self.button = QPushButton('START THE ALGORITHM', self) # Смешная кнопка
        self.button.clicked.connect(self.clicked)
        self.button.setGeometry(0, 66, 500, 34)

    def clicked(self):
        str(algoritm_Evklida(int(self.line_edit.text()), int(self.line_edit_2.text())))
        self.button.setText('RESULT: ' + str(algoritm_Evklida(int(self.line_edit.text()), int(self.line_edit_2.text()))) + '.   PRESS TO START AGAIN')
        
application = QApplication(sys.argv)
window = Example()
window.show()
sys.exit(application.exec_())
