from PySide6.QtCore import Qt,QTextStream,QFile,QIODevice
from PySide6.QtWidgets import QWidget, QFileDialog,QMessageBox
from widget_ui import Ui_Form

class Widget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #hacemos las conexiones
        self.btn_write.clicked.connect(self.write)
        self.btn_read.clicked.connect(self.read)
        self.btn_select.clicked.connect(self.select)


    def write(self):    
        file_name,_=QFileDialog.getSaveFileName(self,"Guardar archivo","",
                                                "Archivo de texto (*.txt)")
        if file_name:
            f=open(file_name,'w')
            f.write(self.txt_edit.toPlainText())
            f.close()
            self.txt_select.setText(file_name)
    
    def read(self):
        file_name=self.txt_select.text()
        f=open(file_name,'r')
        self.txt_edit.setPlainText(f.read())
        f.close()

    def select(self):
        file_name,_=QFileDialog.getOpenFileName(self,"Abrir archivo","",
                                                "Archivo de texto (*.txt)")
        if file_name:
            self.txt_select.setText(file_name)