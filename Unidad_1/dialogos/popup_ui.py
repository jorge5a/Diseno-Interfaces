# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QWidget)

class Ui_popup(object):
    def setupUi(self, popup):
        if not popup.objectName():
            popup.setObjectName(u"popup")
        popup.resize(259, 148)
        self.splitter = QSplitter(popup)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 30, 249, 81))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txt_departamento = QLineEdit(self.widget)
        self.txt_departamento.setObjectName(u"txt_departamento")

        self.horizontalLayout.addWidget(self.txt_departamento)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cmb_so = QComboBox(self.widget1)
        self.cmb_so.addItem("")
        self.cmb_so.addItem("")
        self.cmb_so.addItem("")
        self.cmb_so.addItem("")
        self.cmb_so.setObjectName(u"cmb_so")

        self.horizontalLayout_2.addWidget(self.cmb_so)

        self.splitter.addWidget(self.widget1)
        self.widget2 = QWidget(self.splitter)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_ok = QPushButton(self.widget2)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout_3.addWidget(self.btn_ok)

        self.btn_cancelar = QPushButton(self.widget2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout_3.addWidget(self.btn_cancelar)

        self.splitter.addWidget(self.widget2)

        self.retranslateUi(popup)

        QMetaObject.connectSlotsByName(popup)
    # setupUi

    def retranslateUi(self, popup):
        popup.setWindowTitle(QCoreApplication.translate("popup", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("popup", u"Departamento", None))
        self.label_2.setText(QCoreApplication.translate("popup", u"S.O", None))
        self.cmb_so.setItemText(0, QCoreApplication.translate("popup", u"Windows", None))
        self.cmb_so.setItemText(1, QCoreApplication.translate("popup", u"MacOs", None))
        self.cmb_so.setItemText(2, QCoreApplication.translate("popup", u"Linux", None))
        self.cmb_so.setItemText(3, QCoreApplication.translate("popup", u"Android", None))

        self.btn_ok.setText(QCoreApplication.translate("popup", u"OK", None))
        self.btn_cancelar.setText(QCoreApplication.translate("popup", u"Cancelar", None))
    # retranslateUi

