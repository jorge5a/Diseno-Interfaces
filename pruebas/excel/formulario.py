import sys
from PySide6.QtWidgets import QApplication, QWidget
from formulario_ui import Ui_formulario
from datos_ejemplo import IncluyeAlumno

class formulario(QWidget, Ui_formulario):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #conectores
        self.btn_anadir.clicked.connect(self.anadir)
        self.btn_borrar.clicked.connect(self.borrar)
        self.show()     

    def anadir(self):

        nuevalinea=IncluyeAlumno(
            self.txt_nombre.text(),
            self.txt_edad.text(),
            self.txt_ciudad.text()
        )
         # Obtener los datos de los campos de texto
        
    def borrar(self):
        self.txt_nombre.clear()
        self.txt_edad.clear()
        self.txt_edad_2.clear()