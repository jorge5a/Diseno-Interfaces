# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(503, 454)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dato1 = QTextEdit(self.centralwidget)
        self.dato1.setObjectName(u"dato1")
        self.dato1.setGeometry(QRect(90, 150, 151, 31))
        font = QFont()
        font.setBold(True)
        self.dato1.setFont(font)
        self.dato2 = QTextEdit(self.centralwidget)
        self.dato2.setObjectName(u"dato2")
        self.dato2.setGeometry(QRect(290, 150, 151, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 110, 66, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 110, 66, 20))
        self.boton = QPushButton(self.centralwidget)
        self.boton.setObjectName(u"boton")
        self.boton.setGeometry(QRect(240, 230, 94, 25))
        self.boton.setStyleSheet(u"background-color: rgb(255, 163, 72);")
        self.lcdresultado = QLCDNumber(self.centralwidget)
        self.lcdresultado.setObjectName(u"lcdresultado")
        self.lcdresultado.setGeometry(QRect(350, 310, 91, 51))
        self.resultado = QLabel(self.centralwidget)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(150, 310, 91, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.boton.setText(QCoreApplication.translate("MainWindow", u"Suma", None))
        self.resultado.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

