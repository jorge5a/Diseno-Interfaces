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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(467, 44)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_menos = QPushButton(Widget)
        self.btn_menos.setObjectName(u"btn_menos")
        icon = QIcon()
        icon.addFile(u":/newPrefix/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menos.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_menos)

        self.txt_resultado = QSpinBox(Widget)
        self.txt_resultado.setObjectName(u"txt_resultado")

        self.horizontalLayout.addWidget(self.txt_resultado)

        self.btn_mas = QPushButton(Widget)
        self.btn_mas.setObjectName(u"btn_mas")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.btn_mas.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_mas)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.btn_menos.setText(QCoreApplication.translate("Widget", u"Menos", None))
        self.btn_mas.setText(QCoreApplication.translate("Widget", u"Mas", None))
    # retranslateUi

