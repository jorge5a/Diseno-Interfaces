from PySide6.QtWidgets import QWidget,QInputDialog,QLineEdit
from PySide6.QtCore import QDir
from widget_ui import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QInputDialog Demo")

        #Make the connections
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):

        value, ok = QInputDialog.getInt(self, "Get int", "Select a value : ",150,100,200)
        if (ok) :
            #The f convierte a string el valor          
            self.value_label.setText(f'{value}')     

        #Get text
        """
        text, ok = QInputDialog.getText(self, "getText", "Enter your name : ")
        if (ok and not (text=="")) :
            self.value_label.setText(text)        
        """


      



        
