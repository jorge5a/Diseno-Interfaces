import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo QMessageBox")
        self.resize(300, 200)

        layout = QVBoxLayout()

        btn = QPushButton("Abrir QMessageBox")
        btn.clicked.connect(self.show_messagebox)

        layout.addWidget(btn)
        self.setLayout(layout)

    def show_messagebox(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Mensaje de prueba")
        dialog.setText("Elige una opción:")
        
        # Añadir varios botones
        dialog.setStandardButtons(
            QMessageBox.StandardButton.Ok |
            QMessageBox.StandardButton.Cancel |
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        ret = dialog.exec()  # devuelve el botón pulsado
        print("Valor devuelto (int):", ret)

        if ret == QMessageBox.StandardButton.Ok:
            print("Has pulsado: OK")
        elif ret == QMessageBox.StandardButton.Cancel:
            print("Has pulsado: Cancel")
        elif ret == QMessageBox.StandardButton.Yes:
            print("Has pulsado: Yes")
        elif ret == QMessageBox.StandardButton.No:
            print("Has pulsado: No")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
