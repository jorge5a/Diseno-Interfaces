from PySide6.QtWidgets import QWidget,QDialog
from ejercicio1_ui import Ui_EjercicioDialog
from popup import PopUp

class EjercicioDialog(QWidget, Ui_EjercicioDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_inputinfo.clicked.connect(self.abrir_dialogo)

    def abrir_dialogo(self):
        dialogo=PopUp()
        dialogo.exec()
        if dialogo.result() == QDialog.Accepted:
            nombre=dialogo.txt_nombre.text()
            edad=dialogo.txt_edad.text()
            self.lbl_nombre.setText(nombre)
            self.lbl_edad.setText(edad)


     
