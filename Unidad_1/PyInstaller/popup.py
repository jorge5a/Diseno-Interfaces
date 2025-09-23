from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from popup_ui import Ui_popup

class PopUp(QDialog, Ui_popup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        #esto hace que no se pueda interactuar con la ventana padre hasta cerrar esto
        self.setWindowModality(Qt.ApplicationModal) 

        self.posicion=""
        self.so=""

        self.dbt_menu.clicked.connect(self.buttonbox_clicked)

    def buttonbox_clicked(self, button):
        if button == self.dbt_menu.button(QDialogButtonBox.Ok):
            self.accept()
            
        elif button == self.dbt_menu.button(QDialogButtonBox.Cancel):
            self.reject()
        else:
            print(button.text())
        