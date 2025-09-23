# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(575, 537)
        self.btn_write = QPushButton(Form)
        self.btn_write.setObjectName(u"btn_write")
        self.btn_write.setGeometry(QRect(450, 20, 94, 25))
        self.btn_read = QPushButton(Form)
        self.btn_read.setObjectName(u"btn_read")
        self.btn_read.setGeometry(QRect(450, 50, 94, 25))
        self.txt_edit = QTextEdit(Form)
        self.txt_edit.setObjectName(u"txt_edit")
        self.txt_edit.setGeometry(QRect(20, 20, 411, 381))
        self.btn_select = QPushButton(Form)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setGeometry(QRect(450, 420, 94, 25))
        self.btn_copy = QPushButton(Form)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setGeometry(QRect(450, 470, 94, 25))
        self.txt_select = QLineEdit(Form)
        self.txt_select.setObjectName(u"txt_select")
        self.txt_select.setGeometry(QRect(20, 420, 411, 25))
        self.txt_copy = QLineEdit(Form)
        self.txt_copy.setObjectName(u"txt_copy")
        self.txt_copy.setGeometry(QRect(20, 470, 411, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_write.setText(QCoreApplication.translate("Form", u"Write", None))
        self.btn_read.setText(QCoreApplication.translate("Form", u"Read", None))
        self.btn_select.setText(QCoreApplication.translate("Form", u"Select File", None))
        self.btn_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
    # retranslateUi

