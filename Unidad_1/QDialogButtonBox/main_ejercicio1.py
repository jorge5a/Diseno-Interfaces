import sys
from PySide6.QtWidgets import QApplication

from ejercicio1 import EjercicioDialog

app = QApplication(sys.argv)
window = EjercicioDialog()
window.show()
app.exec()
