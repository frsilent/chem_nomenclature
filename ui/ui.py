# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch.ui'
#
# Created: Sun May  5 16:55:22 2013
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
        MainWindow.resize(848, 494)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.randomButton = QtGui.QPushButton(self.centralwidget)
        self.randomButton.setGeometry(QtCore.QRect(30, 20, 151, 91))
        self.randomButton.setObjectName(_fromUtf8("randomButton"))
        self.animateButton = QtGui.QPushButton(self.centralwidget)
        self.animateButton.setGeometry(QtCore.QRect(670, 60, 131, 91))
        self.animateButton.setObjectName(_fromUtf8("animateButton"))
        self.nomenclatureLabel = QtGui.QLabel(self.centralwidget)
        self.nomenclatureLabel.setGeometry(QtCore.QRect(210, 20, 111, 17))
        self.nomenclatureLabel.setObjectName(_fromUtf8("nomenclatureLabel"))
        self.nomenclatureBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.nomenclatureBox.setGeometry(QtCore.QRect(210, 40, 231, 41))
        self.nomenclatureBox.setObjectName(_fromUtf8("nomenclatureBox"))
        self.guessButton = QtGui.QPushButton(self.centralwidget)
        self.guessButton.setGeometry(QtCore.QRect(210, 90, 91, 27))
        self.guessButton.setObjectName(_fromUtf8("guessButton"))
        self.checkLabel = QtGui.QLabel(self.centralwidget)
        self.checkLabel.setGeometry(QtCore.QRect(510, 50, 101, 31))
        self.checkLabel.setText(_fromUtf8(""))
        self.checkLabel.setObjectName(_fromUtf8("checkLabel"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 130, 600, 300))
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
        self.clearButton.setGeometry(QtCore.QRect(370, 90, 51, 27))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.getNameButton = QtGui.QPushButton(self.centralwidget)
        self.getNameButton.setGeometry(QtCore.QRect(300, 90, 71, 27))
        self.getNameButton.setObjectName(_fromUtf8("getNameButton"))
        self.guessResultLabel = QtGui.QLabel(self.centralwidget)
        self.guessResultLabel.setEnabled(True)
        self.guessResultLabel.setGeometry(QtCore.QRect(210, 120, 111, 17))
        self.guessResultLabel.setVisible(False)
        self.guessResultLabel.setObjectName(_fromUtf8("guessResultLabel"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(630, 230, 211, 201))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(680, 190, 28, 28))
        self.backButton.setStyleSheet(_fromUtf8("background-image: url(../data/back.png);"))
        self.backButton.setText(_fromUtf8(""))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.forwardButton = QtGui.QPushButton(self.centralwidget)
        self.forwardButton.setGeometry(QtCore.QRect(760, 190, 28, 28))
        self.forwardButton.setStyleSheet(_fromUtf8("background-image: url(../data/next.png);"))
        self.forwardButton.setText(_fromUtf8(""))
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(720, 190, 28, 28))
        self.stopButton.setStyleSheet(_fromUtf8("background-image: url(../data/stop.png);"))
        self.stopButton.setText(_fromUtf8(""))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chem Wizard", None))
        self.randomButton.setText(_translate("MainWindow", "Random", None))
        self.animateButton.setText(_translate("MainWindow", "Animate", None))
        self.nomenclatureLabel.setText(_translate("MainWindow", "Nomenclature:", None))
        self.guessButton.setText(_translate("MainWindow", "Submit Guess", None))
        self.clearButton.setText(_translate("MainWindow", "Clear", None))
        self.getNameButton.setText(_translate("MainWindow", "Get Name", None))
        self.guessResultLabel.setText(_translate("MainWindow", "Correct!/Wrong", None))

