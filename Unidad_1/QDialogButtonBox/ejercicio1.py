from PySide6.QtWidgets import QWidget,QDialog
from ejercicio1_ui import Ui_EjercicioDialog
from popup import PopUp

class EjercicioDialog(QWidget, Ui_EjercicioDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ejercicio 1 - Diálogos")#aquí podemos también poner el título
        
        self.btn_inputinfo.clicked.connect(self.abrir_dialogo)
        self.dialogo=PopUp()
        
    def abrir_dialogo(self):
        
        ret=self.dialogo.exec()
        if ret==QDialog.Accepted:
           print(self.dialogo.posicion)
           print(self.dialogo.so)
        else:
           print("Cancelado")