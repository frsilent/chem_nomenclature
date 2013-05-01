__author__ = 'rheintze'

import sys, traceback
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
from ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

from alkane import Alkane
from draw_view import DrawView

class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = DrawView(self.ui.graphicsView)

        self.molecule = None

        #function bindings
        QtCore.QObject.connect(self.ui.validateButton,QtCore.SIGNAL("clicked()"),self.validate)
        QtCore.QObject.connect(self.ui.clearButton,QtCore.SIGNAL("clicked()"),self.clearMolecule)
        QtCore.QObject.connect(self.ui.randomButton,QtCore.SIGNAL("clicked()"),self.view.makeRandom)

    def validate(self):
        carbonMatrix = self.view.getCarbonMatrix()
        try:
            self.molecule = Alkane(carbonMatrix)
        except Exception as error:
            print("Validation Error:")
            print(error)
            print(error.__class__)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=100, file=sys.stdout)

    def clearMolecule(self):
        self.view.clearCarbons()
        for carbon in self.molecule.carbons:
            del carbon
        self.molecule = None

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()

    myapp.show()
    sys.exit(app.exec_())