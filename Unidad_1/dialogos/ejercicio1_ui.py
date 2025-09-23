# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejercicio1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_EjercicioDialog(object):
    def setupUi(self, EjercicioDialog):
        if not EjercicioDialog.objectName():
            EjercicioDialog.setObjectName(u"EjercicioDialog")
        EjercicioDialog.resize(488, 195)
        self.btn_inputinfo = QPushButton(EjercicioDialog)
        self.btn_inputinfo.setObjectName(u"btn_inputinfo")
        self.btn_inputinfo.setGeometry(QRect(300, 10, 164, 25))
        self.lbl_info = QLabel(EjercicioDialog)
        self.lbl_info.setObjectName(u"lbl_info")
        self.lbl_info.setGeometry(QRect(25, 39, 431, 121))

        self.retranslateUi(EjercicioDialog)

        QMetaObject.connectSlotsByName(EjercicioDialog)
    # setupUi

    def retranslateUi(self, EjercicioDialog):
        EjercicioDialog.setWindowTitle(QCoreApplication.translate("EjercicioDialog", u"Form", None))
        self.btn_inputinfo.setText(QCoreApplication.translate("EjercicioDialog", u"Introduce Informaci\u00f3n", None))
        self.lbl_info.setText(QCoreApplication.translate("EjercicioDialog", u"TextLabel", None))
    # retranslateUi

