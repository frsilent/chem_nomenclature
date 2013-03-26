# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch.ui'
#
# Created: Tue Mar 26 11:29:54 2013
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
        MainWindow.resize(1165, 781)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 190, 621, 531))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.chemSpiderView = QtWebKit.QWebView(self.centralwidget)
        self.chemSpiderView.setGeometry(QtCore.QRect(670, 430, 471, 291))
        self.chemSpiderView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.chemSpiderView.setObjectName(_fromUtf8("chemSpiderView"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 400, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.random_pushButton = QtGui.QPushButton(self.centralwidget)
        self.random_pushButton.setGeometry(QtCore.QRect(100, 60, 151, 61))
        self.random_pushButton.setObjectName(_fromUtf8("random_pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 150, 41, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 150, 141, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(280, 150, 141, 31))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.random_pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.random_pushButton_2.setGeometry(QtCore.QRect(300, 60, 151, 61))
        self.random_pushButton_2.setObjectName(_fromUtf8("random_pushButton_2"))
        self.random_pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.random_pushButton_3.setGeometry(QtCore.QRect(760, 250, 271, 101))
        self.random_pushButton_3.setObjectName(_fromUtf8("random_pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Chem Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Additional Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.random_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Random", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "SMILES:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "InChl", None, QtGui.QApplication.UnicodeUTF8))
        self.random_pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.random_pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Animate", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
