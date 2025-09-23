from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit
import sys
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Widgets - QTextEdit")
 
        self.input = QTextEdit(self)
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())