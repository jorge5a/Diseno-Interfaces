# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trabajo2.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Trabajo3(object):
    def setupUi(self, Trabajo3):
        if not Trabajo3.objectName():
            Trabajo3.setObjectName(u"Trabajo3")
        Trabajo3.resize(400, 300)
        self.verticalLayoutWidget = QWidget(Trabajo3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 160, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.horizontalLayoutWidget = QWidget(Trabajo3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(55, 169, 301, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(Trabajo3)

        QMetaObject.connectSlotsByName(Trabajo3)
    # setupUi

    def retranslateUi(self, Trabajo3):
        Trabajo3.setWindowTitle(QCoreApplication.translate("Trabajo3", u"Form", None))
        self.label.setText(QCoreApplication.translate("Trabajo3", u"Hola", None))
        self.pushButton.setText(QCoreApplication.translate("Trabajo3", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Trabajo3", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Trabajo3", u"PushButton", None))
    # retranslateUi

