import sys
from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout,QLineEdit,QPushButton,QTextEdit
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__() # llama al __init__ de QWidget
        self.setWindowTitle('hello app')
        self.setWindowIcon(QIcon('maps.ico'))
        self.resize(500,350)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        #Widgets
        self.inputField = QLineEdit()
        self.button= QPushButton('pincha aqui')
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        text = self.inputField.text()
        self.output.append(text)



app= QApplication(sys.argv)

window =MyApp()
window.show()

app.exec()


