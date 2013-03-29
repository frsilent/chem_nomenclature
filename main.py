__author__ = 'rheintze'

import sys
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.smilesBox,QtCore.SIGNAL("textChanged()"),self.smiles_changed)
        #QtCore.QObject.connect(self.ui.smilesBox,QtCore.SIGNAL("textChanged()"),self.smiles_changed)

    def smiles_changed(self):
        self.ui.inchlBox.setPlainText('omg!')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())