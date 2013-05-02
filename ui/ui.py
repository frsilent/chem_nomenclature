# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch.ui'
#
# Created: Wed May  1 11:19:46 2013
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
        MainWindow.resize(635, 560)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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
        self.animateButton.setGeometry(QtCore.QRect(520, 40, 81, 41))
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
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 200, 600, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(600, 300))
        self.graphicsView.setMaximumSize(QtCore.QSize(600, 300))
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 600.0, 300.0))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(310, 90, 51, 27))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.validateButton = QtGui.QPushButton(self.centralwidget)
        self.validateButton.setGeometry(QtCore.QRect(370, 90, 87, 27))
        self.validateButton.setObjectName(_fromUtf8("validateButton"))
        self.guessResultLabel = QtGui.QLabel(self.centralwidget)
        self.guessResultLabel.setEnabled(True)
        self.guessResultLabel.setGeometry(QtCore.QRect(210, 120, 111, 17))
        self.guessResultLabel.setVisible(False)
        self.guessResultLabel.setObjectName(_fromUtf8("guessResultLabel"))
        self.renderButton = QtGui.QPushButton(self.centralwidget)
        self.renderButton.setGeometry(QtCore.QRect(470, 130, 98, 27))
        self.renderButton.setObjectName(_fromUtf8("renderButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Chem Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.randomButton.setText(QtGui.QApplication.translate("MainWindow", "Random", None, QtGui.QApplication.UnicodeUTF8))
        self.smilesLabel.setText(QtGui.QApplication.translate("MainWindow", "SMILES:", None, QtGui.QApplication.UnicodeUTF8))
        self.inchiLabel.setText(QtGui.QApplication.translate("MainWindow", "InChi", None, QtGui.QApplication.UnicodeUTF8))
        self.animateButton.setText(QtGui.QApplication.translate("MainWindow", "Animate", None, QtGui.QApplication.UnicodeUTF8))
        self.nomenclatureLabel.setText(QtGui.QApplication.translate("MainWindow", "Nomenclature:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkButton.setText(QtGui.QApplication.translate("MainWindow", "Check!", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.validateButton.setText(QtGui.QApplication.translate("MainWindow", "Validate", None, QtGui.QApplication.UnicodeUTF8))
        self.guessResultLabel.setText(QtGui.QApplication.translate("MainWindow", "Correct!/Wrong", None, QtGui.QApplication.UnicodeUTF8))
        self.renderButton.setText(QtGui.QApplication.translate("MainWindow", "Render", None, QtGui.QApplication.UnicodeUTF8))

