import sys

# 1. Importar QApplication y los widgets requeridos
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow



app = QApplication([])



# 3. Creamos la aplicación GUI
window = QMainWindow()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
window.show()
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# Execute the application. 
# Aseguramos que el código de salida de la aplicación Qt 
# se devuelve al sistema operativo con sys.exit()
sys.exit(app.exec())