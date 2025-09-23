# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormularioCalculadora.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 100, 31, 28))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 100, 31, 28))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 100, 31, 28))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 140, 31, 28))
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(150, 140, 31, 28))
        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(190, 140, 31, 28))
        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(110, 180, 31, 28))
        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(150, 180, 31, 28))
        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(190, 180, 31, 28))
        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(260, 90, 93, 28))
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(260, 130, 93, 28))
        self.pushButton_12 = QPushButton(Dialog)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(260, 170, 93, 28))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 141, 16))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Sumar", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Restar", None))
        self.pushButton_12.setText(QCoreApplication.translate("Dialog", u"Multiplicar", None))
        self.label.setText("")
    # retranslateUi

