# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSplitter, QWidget)

class Ui_formulario(object):
    def setupUi(self, formulario):
        if not formulario.objectName():
            formulario.setObjectName(u"formulario")
        formulario.resize(267, 176)
        self.splitter_4 = QSplitter(formulario)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(30, 30, 198, 75))
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.splitter = QSplitter(self.splitter_4)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.txt_nombre = QLineEdit(self.splitter)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.splitter.addWidget(self.txt_nombre)
        self.splitter_4.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.txt_edad = QLineEdit(self.splitter_2)
        self.txt_edad.setObjectName(u"txt_edad")
        self.splitter_2.addWidget(self.txt_edad)
        self.splitter_4.addWidget(self.splitter_2)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.splitter_3.addWidget(self.label_3)
        self.txt_ciudad = QLineEdit(self.splitter_3)
        self.txt_ciudad.setObjectName(u"txt_ciudad")
        self.splitter_3.addWidget(self.txt_ciudad)
        self.splitter_4.addWidget(self.splitter_3)
        self.splitter_5 = QSplitter(formulario)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(50, 120, 160, 25))
        self.splitter_5.setOrientation(Qt.Orientation.Horizontal)
        self.btn_anadir = QPushButton(self.splitter_5)
        self.btn_anadir.setObjectName(u"btn_anadir")
        self.splitter_5.addWidget(self.btn_anadir)
        self.btn_borrar = QPushButton(self.splitter_5)
        self.btn_borrar.setObjectName(u"btn_borrar")
        self.splitter_5.addWidget(self.btn_borrar)

        self.retranslateUi(formulario)

        QMetaObject.connectSlotsByName(formulario)
    # setupUi

    def retranslateUi(self, formulario):
        formulario.setWindowTitle(QCoreApplication.translate("formulario", u"Form", None))
        self.label.setText(QCoreApplication.translate("formulario", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("formulario", u"Edad", None))
        self.label_3.setText(QCoreApplication.translate("formulario", u"Ciudad", None))
        self.btn_anadir.setText(QCoreApplication.translate("formulario", u"A\u00f1adir", None))
        self.btn_borrar.setText(QCoreApplication.translate("formulario", u"Borrar", None))
    # retranslateUi

