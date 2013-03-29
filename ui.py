# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch.ui'
#
# Created: Fri Mar 29 15:45:25 2013
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
        self.chemSpider_label = QtGui.QLabel(self.centralwidget)
        self.chemSpider_label.setGeometry(QtCore.QRect(670, 400, 101, 17))
        self.chemSpider_label.setObjectName(_fromUtf8("chemSpider_label"))
        self.random_pushButton = QtGui.QPushButton(self.centralwidget)
        self.random_pushButton.setGeometry(QtCore.QRect(100, 60, 151, 61))
        self.random_pushButton.setObjectName(_fromUtf8("random_pushButton"))
        self.smiles_label = QtGui.QLabel(self.centralwidget)
        self.smiles_label.setGeometry(QtCore.QRect(20, 160, 51, 16))
        self.smiles_label.setObjectName(_fromUtf8("smiles_label"))
        self.inchl_label = QtGui.QLabel(self.centralwidget)
        self.inchl_label.setGeometry(QtCore.QRect(240, 150, 41, 17))
        self.inchl_label.setObjectName(_fromUtf8("inchl_label"))
        self.smilesBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.smilesBox.setGeometry(QtCore.QRect(70, 150, 141, 31))
        self.smilesBox.setObjectName(_fromUtf8("smilesBox"))
        self.inchlBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.inchlBox.setGeometry(QtCore.QRect(280, 150, 141, 31))
        self.inchlBox.setObjectName(_fromUtf8("inchlBox"))
        self.create_pushButton = QtGui.QPushButton(self.centralwidget)
        self.create_pushButton.setGeometry(QtCore.QRect(300, 60, 151, 61))
        self.create_pushButton.setObjectName(_fromUtf8("create_pushButton"))
        self.animate_pushButton = QtGui.QPushButton(self.centralwidget)
        self.animate_pushButton.setGeometry(QtCore.QRect(760, 200, 271, 101))
        self.animate_pushButton.setObjectName(_fromUtf8("animate_pushButton"))
        self.nomenclature_label = QtGui.QLabel(self.centralwidget)
        self.nomenclature_label.setGeometry(QtCore.QRect(640, 50, 111, 17))
        self.nomenclature_label.setObjectName(_fromUtf8("nomenclature_label"))
        self.nomenclatureBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.nomenclatureBox.setGeometry(QtCore.QRect(640, 70, 281, 41))
        self.nomenclatureBox.setObjectName(_fromUtf8("nomenclatureBox"))
        self.check_pushButton = QtGui.QPushButton(self.centralwidget)
        self.check_pushButton.setGeometry(QtCore.QRect(640, 120, 87, 27))
        self.check_pushButton.setObjectName(_fromUtf8("check_pushButton"))
        self.check_label = QtGui.QLabel(self.centralwidget)
        self.check_label.setGeometry(QtCore.QRect(940, 80, 101, 31))
        self.check_label.setText(_fromUtf8(""))
        self.check_label.setObjectName(_fromUtf8("check_label"))
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
        self.chemSpider_label.setText(QtGui.QApplication.translate("MainWindow", "Additional Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.random_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Random", None, QtGui.QApplication.UnicodeUTF8))
        self.smiles_label.setText(QtGui.QApplication.translate("MainWindow", "SMILES:", None, QtGui.QApplication.UnicodeUTF8))
        self.inchl_label.setText(QtGui.QApplication.translate("MainWindow", "InChl", None, QtGui.QApplication.UnicodeUTF8))
        self.create_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.animate_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Animate", None, QtGui.QApplication.UnicodeUTF8))
        self.nomenclature_label.setText(QtGui.QApplication.translate("MainWindow", "Nomenclature:", None, QtGui.QApplication.UnicodeUTF8))
        self.check_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Check!", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
