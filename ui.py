# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch.ui'
#
# Created: Sun Apr 14 20:52:55 2013
#      by: PyQt4 UI code generator 4.9.1
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
        self.chemSpiderView = QtWebKit.QWebView(self.centralwidget)
        self.chemSpiderView.setGeometry(QtCore.QRect(610, 150, 181, 401))
        self.chemSpiderView.setProperty("url", QtCore.QUrl(_fromUtf8("about:blank")))
        self.chemSpiderView.setObjectName(_fromUtf8("chemSpiderView"))
        self.chemSpiderLabel = QtGui.QLabel(self.centralwidget)
        self.chemSpiderLabel.setGeometry(QtCore.QRect(670, 100, 101, 17))
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
        self.animateButton.setGeometry(QtCore.QRect(540, 10, 201, 71))
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
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 200, 625, 325))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(625, 325))
        self.graphicsView.setMaximumSize(QtCore.QSize(625, 325))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 600.0, 300.0))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Chem Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.chemSpiderLabel.setText(QtGui.QApplication.translate("MainWindow", "Additional Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.randomButton.setText(QtGui.QApplication.translate("MainWindow", "Random", None, QtGui.QApplication.UnicodeUTF8))
        self.smilesLabel.setText(QtGui.QApplication.translate("MainWindow", "SMILES:", None, QtGui.QApplication.UnicodeUTF8))
        self.inchiLabel.setText(QtGui.QApplication.translate("MainWindow", "InChi", None, QtGui.QApplication.UnicodeUTF8))
        self.animateButton.setText(QtGui.QApplication.translate("MainWindow", "Animate", None, QtGui.QApplication.UnicodeUTF8))
        self.nomenclatureLabel.setText(QtGui.QApplication.translate("MainWindow", "Nomenclature:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkButton.setText(QtGui.QApplication.translate("MainWindow", "Check!", None, QtGui.QApplication.UnicodeUTF8))
        self.generateButton.setText(QtGui.QApplication.translate("MainWindow", "Generate", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
