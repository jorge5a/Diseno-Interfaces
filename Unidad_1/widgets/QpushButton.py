from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import Qt
import sys
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("Widgets")
 
        button = QPushButton("Hello World", self)
        button.move(100, 100)
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())