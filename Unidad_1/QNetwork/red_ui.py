# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'red.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(695, 300)
        self.txt_output = QTextBrowser(Form)
        self.txt_output.setObjectName(u"txt_output")
        self.txt_output.setGeometry(QRect(20, 61, 651, 221))
        self.btn_obtener = QPushButton(Form)
        self.btn_obtener.setObjectName(u"btn_obtener")
        self.btn_obtener.setGeometry(QRect(580, 10, 94, 25))
        self.txt_input = QLineEdit(Form)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setGeometry(QRect(30, 10, 501, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Obtener contenido", None))
        self.btn_obtener.setText(QCoreApplication.translate("Form", u"Obtener", None))
        self.txt_input.setText(QCoreApplication.translate("Form", u"https://jsonplaceholder.typicode.com/todos/1", None))
    # retranslateUi

