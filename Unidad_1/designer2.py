import sys
from PyQt6 import uic, QtWidgets

# Cargar el archivo .ui creado con Qt Designer
# la clase base 'QMainWindow' se cargan desde el archivo .ui
formulario = "designer2.ui"
#se encarga de leer y analizar el archivo XML, así como de generar las clases de Python necesarias para crear la interfaz de usuario.
#QtBaseClass es la clase base de la ventana principal, que en este caso es QMainWindow.
#formularioPrincipal es la clase que contiene los elementos de la interfaz de usuario definidos en el archivo .ui.
formularioPrincipal, QtBaseClass = uic.loadUiType(formulario)

# Definir la clase principal de la ventana
class VentanaPrincipal(QtBaseClass, formularioPrincipal):
    def __init__(self):
        # Inicializar la ventana principal y la interfaz de usuario
        super(VentanaPrincipal, self).__init__()
        self.setupUi(self)

        # Conectar el botón 'Suma' a una función
        # Cuando se haga clic en el botón 'boton', se ejecutará la función 'suma'
        self.boton.clicked.connect(self.suma)

    def suma(self):
        # Obtener el texto de los cuadros de texto 'dato1' y 'dato2'
        # Convertir el texto a números enteros
        try:
            dato1 = int(self.dato1.toPlainText())
            dato2 = int(self.dato2.toPlainText())
            # Realizar la suma
            resultado = dato1 + dato2
            # Mostrar el resultado en el QLCDNumber llamado 'lcdresultado'
            self.lcdresultado.display(resultado)
        except ValueError:
            # Manejar el error si los datos no son números
            self.lcdresultado.display("Error")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())