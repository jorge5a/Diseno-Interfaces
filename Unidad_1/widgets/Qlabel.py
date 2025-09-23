from PyQt6.QtWidgets import  QApplication, QWidget, QLabel
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Qwidgets - QLabel")

        label = QLabel("Esto es unn Qlabel", self)
        label.move(80, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())