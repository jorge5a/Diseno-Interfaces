from PySide6.QtWidgets import QWidget,QFontDialog
from PySide6.QtGui import QFont
from widget_ui import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFontDialog Demo")
        self.button.clicked.connect(self.button_clicked)


    def button_clicked(self):
    
        ok,font = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 20),self)
        if ok:
            self.lbl_out.setFont(font)
        else:
            print("NO se ha seleccionado una fuente válida")  