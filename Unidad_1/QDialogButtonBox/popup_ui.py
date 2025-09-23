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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSplitter, QWidget)

class Ui_popup(object):
    def setupUi(self, popup):
        if not popup.objectName():
            popup.setObjectName(u"popup")
        popup.resize(552, 206)
        self.splitter = QSplitter(popup)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 30, 249, 81))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txt_departamento = QLineEdit(self.layoutWidget)
        self.txt_departamento.setObjectName(u"txt_departamento")

        self.horizontalLayout.addWidget(self.txt_departamento)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cmb_so = QComboBox(self.layoutWidget1)
        self.cmb_so.addItem("")
        self.cmb_so.addItem("")
        self.cmb_so.addItem("")
        self.cmb_so.addItem("")
        self.cmb_so.setObjectName(u"cmb_so")

        self.horizontalLayout_2.addWidget(self.cmb_so)

        self.splitter.addWidget(self.layoutWidget1)
        self.dbt_menu = QDialogButtonBox(popup)
        self.dbt_menu.setObjectName(u"dbt_menu")
        self.dbt_menu.setGeometry(QRect(50, 140, 461, 25))
        self.dbt_menu.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Open|QDialogButtonBox.StandardButton.Save|QDialogButtonBox.StandardButton.SaveAll)

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

    # retranslateUi

