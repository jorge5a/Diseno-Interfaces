from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from popup_ui import Ui_popup

class PopUp(QDialog, Ui_popup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        #esto hace que no se pueda interactuar con la ventana padre hasta cerrar esto
        self.setWindowModality(Qt.ApplicationModal) 

        self.posicion=""
        self.so=""

        self.btn_ok.clicked.connect(self.aceptar)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        self.posicion = self.txt_departamento.text()
        self.so = self.cmb_so.currentText()
        self.accept()

    def cancelar(self):
        self.reject()