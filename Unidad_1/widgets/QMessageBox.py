from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QMessageBox
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Widgets - QMessageBox")
 
        dialog = QMessageBox(parent=self, text="Hello World")
        dialog.setWindowTitle("Message Dialog")
        ret = dialog.exec()   # Stores the return value for the button pressed
        print("Return value:", ret)
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())