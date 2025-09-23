import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QDialog,
    QVBoxLayout, QPushButton, QLabel
)


# ------------------------
# Ventana principal con QMainWindow
# ------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMainWindow - Ventana Principal")

        # Widget central obligatorio en QMainWindow
        central_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Soy un QMainWindow"))
        btn_dialog = QPushButton("Abrir QDialog")
        btn_widget = QPushButton("Abrir QWidget simple")

        btn_dialog.clicked.connect(self.abrir_dialogo)
        btn_widget.clicked.connect(self.abrir_widget)

        layout.addWidget(btn_dialog)
        layout.addWidget(btn_widget)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def abrir_dialogo(self):
        dialog = MyDialog(self)
        dialog.exec()   # QDialog modal (bloquea hasta cerrar)

    def abrir_widget(self):
        self.w = SimpleWidget()   # mantener referencia
        self.w.show()


# ------------------------
# QDialog (ventana de diálogo)
# ------------------------
class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QDialog - Ventana de diálogo")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Soy un QDialog"))
        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)
        self.setLayout(layout)


# ------------------------
# QWidget simple
# ------------------------
class SimpleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget - Ventana simple")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Soy un QWidget"))
        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)
        self.setLayout(layout)


# ------------------------
# Programa principal
# ------------------------
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
