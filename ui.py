# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch.ui'
#
# Created: Sun Apr  7 16:10:36 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1165, 781)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 190, 871, 531))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.chemSpiderView = QtWebKit.QWebView(self.centralwidget)
        self.chemSpiderView.setGeometry(QtCore.QRect(910, 430, 231, 291))
        self.chemSpiderView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.chemSpiderView.setObjectName(_fromUtf8("chemSpiderView"))
        self.chemSpiderLabel = QtGui.QLabel(self.centralwidget)
        self.chemSpiderLabel.setGeometry(QtCore.QRect(910, 390, 101, 17))
        self.chemSpiderLabel.setObjectName(_fromUtf8("chemSpiderLabel"))
        self.randomButton = QtGui.QPushButton(self.centralwidget)
        self.randomButton.setGeometry(QtCore.QRect(30, 20, 151, 91))
        self.randomButton.setObjectName(_fromUtf8("randomButton"))
        self.smilesLabel = QtGui.QLabel(self.centralwidget)
        self.smilesLabel.setGeometry(QtCore.QRect(20, 160, 51, 16))
        self.smilesLabel.setObjectName(_fromUtf8("smilesLabel"))
        self.inchiLabel = QtGui.QLabel(self.centralwidget)
        self.inchiLabel.setGeometry(QtCore.QRect(240, 150, 41, 17))
        self.inchiLabel.setObjectName(_fromUtf8("inchiLabel"))
        self.smilesBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.smilesBox.setGeometry(QtCore.QRect(70, 150, 141, 31))
        self.smilesBox.setObjectName(_fromUtf8("smilesBox"))
        self.inchiBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.inchiBox.setGeometry(QtCore.QRect(280, 150, 141, 31))
        self.inchiBox.setObjectName(_fromUtf8("inchiBox"))
        self.animateButton = QtGui.QPushButton(self.centralwidget)
        self.animateButton.setGeometry(QtCore.QRect(940, 280, 201, 71))
        self.animateButton.setObjectName(_fromUtf8("animateButton"))
        self.nomenclatureLabel = QtGui.QLabel(self.centralwidget)
        self.nomenclatureLabel.setGeometry(QtCore.QRect(210, 20, 111, 17))
        self.nomenclatureLabel.setObjectName(_fromUtf8("nomenclatureLabel"))
        self.nomenclatureBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.nomenclatureBox.setGeometry(QtCore.QRect(210, 40, 281, 41))
        self.nomenclatureBox.setObjectName(_fromUtf8("nomenclatureBox"))
        self.checkButton = QtGui.QPushButton(self.centralwidget)
        self.checkButton.setGeometry(QtCore.QRect(210, 90, 87, 27))
        self.checkButton.setObjectName(_fromUtf8("checkButton"))
        self.checkLabel = QtGui.QLabel(self.centralwidget)
        self.checkLabel.setGeometry(QtCore.QRect(510, 50, 101, 31))
        self.checkLabel.setText(_fromUtf8(""))
        self.checkLabel.setObjectName(_fromUtf8("checkLabel"))
        self.generateButton = QtGui.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(440, 150, 87, 27))
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chem Wizard", None))
        self.chemSpiderLabel.setText(_translate("MainWindow", "Additional Info:", None))
        self.randomButton.setText(_translate("MainWindow", "Random", None))
        self.smilesLabel.setText(_translate("MainWindow", "SMILES:", None))
        self.inchiLabel.setText(_translate("MainWindow", "InChi", None))
        self.animateButton.setText(_translate("MainWindow", "Animate", None))
        self.nomenclatureLabel.setText(_translate("MainWindow", "Nomenclature:", None))
        self.checkButton.setText(_translate("MainWindow", "Check!", None))
        self.generateButton.setText(_translate("MainWindow", "Generate", None))

from PyQt4 import QtWebKit
