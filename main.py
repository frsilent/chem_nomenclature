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

        #QtCore.QObject.connect(self.ui.smilesBox,QtCore.SIGNAL("textChanged()"),self.changeInchi)
        #QtCore.QObject.connect(self.ui.inchiBox,QtCore.SIGNAL("textChanged()"),self.enableInchi)


        QtCore.QObject.connect(self.ui.smilesBox,QtCore.SIGNAL("leaveEvent()"), self.changeInchi)

        #QtCore.QObject.connect(self.ui.generate_pushButton,QtCore.SIGNAL("clicked()"),self.generate)

    def changeInchi(self):
        print('Yahoo!!!!!!!')
        self.ui.inchiBox.setPlainText('omg')

    def generate(self):
        target = Alkane(self.ui.inchiBox.toPlainText())
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())