from PySide6.QtWidgets import QApplication
from formulario import formulario
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = formulario()
    sys.exit(app.exec())