__author__ = 'rheintze'

import sys
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

from Alkane import Alkane

class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.target = None

        QtCore.QObject.connect(self.ui.generateButton,QtCore.SIGNAL("clicked()"),self.generate)

    def generate(self):
        #target = Alkane(self.ui.inchiBox.toPlainText())
        print(str(self.ui.inchiBox.toPlainText()))
    def makeCarbon(self):
        print("graphicsView clicked in")

    def draw(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.target = Alkane('CC')

    myapp.show()
    sys.exit(app.exec_())