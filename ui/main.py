__author__ = 'rheintze'

import sys, traceback
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

from chemistry.alkane import Alkane
from chemistry.chem_exceptions import *
from carbon_view import CarbonView
from Animation import Animation
from network import chemspipy

class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = CarbonView(self.ui.graphicsView)

        self.molecule = None

        #function bindings
        QtCore.QObject.connect(self.ui.guessButton,QtCore.SIGNAL("clicked()"),self.guessButton)
        QtCore.QObject.connect(self.ui.clearButton,QtCore.SIGNAL("clicked()"),self.clearMolecule)
        QtCore.QObject.connect(self.ui.getNameButton,QtCore.SIGNAL("clicked()"),self.getName)
        QtCore.QObject.connect(self.ui.animateButton,QtCore.SIGNAL("clicked()"),self.animate)
        QtCore.QObject.connect(self.ui.randomButton,QtCore.SIGNAL("clicked()"),self.makeRandom)
        QtCore.QObject.connect(self.ui.additionalButton,QtCore.SIGNAL("clicked()"),self.getWebInfo)
        
        self.animation = Animation()

    def guessButton(self):
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
        self.view.clearImages()
        self.molecule = None

    def getName(self):
        carbonMatrix = self.view.getCarbonMatrix()
        try:
            self.molecule = Alkane(carbonMatrix)
            self.ui.nomenclatureBox.setPlainText(self.molecule.getName())
        except EmptyAlkaneError:
            self.ui.nomenclatureBox.setPlainText("Please click in the grid to add carbons")
        except CyclicAlkaneError:
            self.ui.nomenclatureBox.setPlainText("The molecule contains a loop or a block.")
        except BranchingCarbonChainError:
            self.ui.nomenclatureBox.setPlainText("Only straight-chain substituents are supported.")
        except AlkaneNotConnectedError:
            self.ui.nomenclatureBox.setPlainText("Not all of the carbons are connected.")

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

    def animate(self):
        self.view.clearImages()
        self.view.passAlkane(self.molecule)

    def getWebInfo(self):
        webMolecule = chemspipy.find_one(self.molecule.getName())
        webMolecule.loadextendedcompoundinfo()
        infoString = "Common Name: " + str(webMolecule.commonname)
        infoString += "\nAverage Mass: " + str(webMolecule.averagemass)
        infoString += "\nMolecular Weight: " + str(webMolecule.molecularweight)
        infoString += "\nMono Isotopic Mass: " + str(webMolecule.monoisotopicmass)
        infoString += "\nNominal Mass: " + str(webMolecule.nominalmass)

        self.ui.informationText.setPlainText(infoString)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()

    myapp.show()
    sys.exit(app.exec_())