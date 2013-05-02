__author__ = 'rheintze'

import sys, traceback
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

from chemistry.alkane import Alkane
from carbon_view import CarbonView

class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = CarbonView(self.ui.graphicsView)

        self.molecule = None

        #function bindings
        QtCore.QObject.connect(self.ui.validateButton,QtCore.SIGNAL("clicked()"),self.validate)
        QtCore.QObject.connect(self.ui.clearButton,QtCore.SIGNAL("clicked()"),self.clearMolecule)
        QtCore.QObject.connect(self.ui.checkButton,QtCore.SIGNAL("clicked()"),self.checkGuess)
        QtCore.QObject.connect(self.ui.animateButton,QtCore.SIGNAL("clicked()"),self.view.animate)
        QtCore.QObject.connect(self.ui.randomButton,QtCore.SIGNAL("clicked()"),self.makeRandom)
        QtCore.QObject.connect(self.ui.renderButton,QtCore.SIGNAL("clicked()"),self.renderAlkane)

    def validate(self):
        carbonMatrix = self.view.getCarbonMatrix()
        try:
            self.molecule = Alkane(carbonMatrix)
        except Exception as error:
            print("Validation Error:")
            print(error)
            print(error.__class__)
            exc_traceback = sys.exc_info()[2]
            traceback.print_tb(exc_traceback, limit=100, file=sys.stdout)

    def clearMolecule(self):
        self.view.clearCarbons()
        for carbon in self.molecule.carbons:
            del carbon
#        self.molecule = None

    def checkGuess(self):
        try:
            self.ui.guessResultLabel.setVisible(True)
            self.molecule.verify(self.ui.nomenclatureBox.toPlainText)
            if self.molecule.verify(self.ui.nomenclatureBox.toPlainText):
                self.ui.guessResultLabel.setText("Correct!")
            else:
                self.ui.guessResultLabel.setText("Incorrect")
        except Exception as error:
            print("Guess not made or molecule does not exist")
            print(error)
            print(error.__class__)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=100, file=sys.stdout)

    def renderAlkane(self):
        self.view.setScreenToAlkane(self.molecule)
        
    def makeRandom(self):
        #TODO: Make and display random Alkane
        pass
    
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()

    myapp.show()
    sys.exit(app.exec_())