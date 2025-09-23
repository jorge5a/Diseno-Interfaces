from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("CodersLegacy")
 
        self.radio = QCheckBox("Option 1", self)
        self.radio.toggled.connect(self.showDetails)
        self.radio.move(100, 100)
 
    def showDetails(self):
        print("Selected: ", self.sender().isChecked(),
              "  Name: ", self.sender().text())
        # self.sender() gives ref to widget that emitted signal
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())