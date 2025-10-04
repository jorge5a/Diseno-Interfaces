from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from widget_ui import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
        self.txt_resultado.setValue(50)
        self.btn_mas.clicked.connect(self.plus)
        self.btn_menos.clicked.connect(self.minus)

       


    def plus(self):
        value = self.txt_resultado.value()
        self.txt_resultado.setValue(value + 1)

    def minus(self):
        value = self.txt_resultado.value()
        self.txt_resultado.setValue(value - 1)
