import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication(sys.argv)
loader = QUiLoader()

f = QFile("FormularioCalculadora.ui")
f.open(QFile.ReadOnly)
window = loader.load(f, None)
f.close()
if window is None:
    raise SystemExit("No se pudo cargar FormularioCalculadora.ui")

label = window.findChild(QLabel, "label")

boton1 = window.findChild(QWidget, "pushButton")
boton2 = window.findChild(QWidget, "pushButton_2")
boton3 = window.findChild(QWidget, "pushButton_3")
boton4 = window.findChild(QWidget, "pushButton_4")
boton5 = window.findChild(QWidget, "pushButton_5")
boton6 = window.findChild(QWidget, "pushButton_6")
boton7 = window.findChild(QWidget, "pushButton_7")
boton8 = window.findChild(QWidget, "pushButton_8")
boton9 = window.findChild(QWidget, "pushButton_9")
botonSumar = window.findChild(QWidget, "pushButton_10")
botonRestar = window.findChild(QWidget, "pushButton_11")

def poner1(): label.setText(label.text() + "1")
def poner2(): label.setText(label.text() + "2")
def poner3(): label.setText(label.text() + "3")
def poner4(): label.setText(label.text() + "4")
def poner5(): label.setText(label.text() + "5")
def poner6(): label.setText(label.text() + "6")
def poner7(): label.setText(label.text() + "7")
def poner8(): label.setText(label.text() + "8")
def poner9(): label.setText(label.text() + "9")
def ponerMas(): label.setText(label.text() + "+")
def ponerMenos(): label.setText(label.text() + "-")

boton1.clicked.connect(poner1)
boton2.clicked.connect(poner2)
boton3.clicked.connect(poner3)
boton4.clicked.connect(poner4)
boton5.clicked.connect(poner5)
boton6.clicked.connect(poner6)
boton7.clicked.connect(poner7)
boton8.clicked.connect(poner8)
boton9.clicked.connect(poner9)
if botonSumar: botonSumar.clicked.connect(ponerMas)
if botonRestar: botonRestar.clicked.connect(ponerMenos)

window.setWindowTitle("Calculadora (UI)")
window.show()
sys.exit(app.exec())