# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designericons.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(690, 475)
        self.actionaptdo1 = QAction(MainWindow)
        self.actionaptdo1.setObjectName(u"actionaptdo1")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.actionaptdo1.setIcon(icon)
        self.actionaptado2 = QAction(MainWindow)
        self.actionaptado2.setObjectName(u"actionaptado2")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.actionaptado2.setIcon(icon1)
        self.actionotros = QAction(MainWindow)
        self.actionotros.setObjectName(u"actionotros")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 690, 22))
        self.menuTest = QMenu(self.menubar)
        self.menuTest.setObjectName(u"menuTest")
        self.menuMenu2 = QMenu(self.menubar)
        self.menuMenu2.setObjectName(u"menuMenu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuMenu2.menuAction())
        self.menuTest.addAction(self.actionaptdo1)
        self.menuTest.addAction(self.actionaptado2)
        self.menuTest.addSeparator()
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionotros)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionaptdo1)
        self.toolBar.addAction(self.actionaptado2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionaptdo1.setText(QCoreApplication.translate("MainWindow", u"aptdo1", None))
        self.actionaptado2.setText(QCoreApplication.translate("MainWindow", u"aptado2", None))
        self.actionotros.setText(QCoreApplication.translate("MainWindow", u"otros", None))
        self.menuTest.setTitle(QCoreApplication.translate("MainWindow", u"Menu1", None))
        self.menuMenu2.setTitle(QCoreApplication.translate("MainWindow", u"Menu2", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

