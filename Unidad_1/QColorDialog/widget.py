from PySide6.QtWidgets import QWidget,QFontDialog,QColorDialog
from PySide6.QtGui import QFont, QPalette
from widget_ui import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFontDialog Demo")
        self.lbl_out.setAutoFillBackground(True)  #Permite el cambio de color de fondo

        #Make the connections
        self.text_color_button.clicked.connect(self.set_color)
        self.background_color_button.clicked.connect(self.set_background)
        
        self.font_button.clicked.connect(self.set_font)

    def set_color(self):
        palette = self.lbl_out.palette()
        color = palette.color(QPalette.WindowText)
        chosenColor = QColorDialog.getColor(color,self,"Choose text color")

        if(chosenColor.isValid()):
            palette.setColor(QPalette.WindowText,chosenColor)
            self.lbl_out.setPalette(palette)
        else:
            print("User chose a bad text color")


    def set_background(self):
        palette = self.lbl_out.palette()
        color = palette.color(QPalette.Window)
        chosenColor = QColorDialog.getColor(color,self,"Choose background color")

        if(chosenColor.isValid()):
            palette.setColor(QPalette.Window,chosenColor)
            self.lbl_out.setPalette(palette)
        else:
            print("User chose a bad background color")


    def set_font(self):
    
        ok,font = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 20),self)
        if ok:
            self.lbl_out.setFont(font)
        else:
            print("User didn't select any valid font")  