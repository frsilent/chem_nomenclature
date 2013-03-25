# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch.ui'
#
# Created: Mon Mar 25 15:08:33 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(25, 141, 511, 401))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_additional = QtGui.QLabel(self.centralwidget)
        self.label_additional.setGeometry(QtCore.QRect(560, 350, 141, 21))
        self.label_additional.setObjectName(_fromUtf8("label_additional"))
        self.chemSpiderView = QtWebKit.QWebView(self.centralwidget)
        self.chemSpiderView.setGeometry(QtCore.QRect(550, 370, 231, 171))
        self.chemSpiderView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.chemSpiderView.setObjectName(_fromUtf8("chemSpiderView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Chem Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_additional.setText(QtGui.QApplication.translate("MainWindow", "Additional Info:", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
