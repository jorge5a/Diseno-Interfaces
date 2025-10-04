from PySide6.QtWidgets import QWidget
from red_ui import Ui_Form
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl

class Red(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # --- 1) Crear el gestor de red ---
        # Este objeto se encarga de realizar las peticiones (GET, POST, etc.)
        self.manager = QNetworkAccessManager()

        # --- 2) Conectar la señal finished al método que procesará la respuesta ---
        # Cuando cualquier petición termine, se llamará a self.respuesta_recibida(reply)
        self.manager.finished.connect(self.respuesta_recibida)

        # --- Evento del botón ---
        self.btn_obtener.clicked.connect(self.hacer_peticion)

    def hacer_peticion(self):
        # Creamos la URL de destino (una API pública de ejemplo)
        url = QUrl(self.txt_input.text())
        # Creamos el objeto QNetworkRequest con esa URL
        request = QNetworkRequest(url)
        # Llamamos a .get() para lanzar una petición HTTP GET
        # Esto no bloquea la interfaz: Qt lo hace en segundo plano
        self.manager.get(request)  

    def respuesta_recibida(self, reply):
        # Se ejecuta cuando se completa la petición
        
        data = reply.readAll()
        texto = bytes(data).decode("utf-8")
        self.txt_output.setPlainText(texto)
