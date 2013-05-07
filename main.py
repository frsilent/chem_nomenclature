import sys, traceback
from PyQt4 import QtCore, QtGui
from ui.ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

from chemistry.alkane import Alkane
from chemistry.chem_exceptions import *
from ui.carbon_view import CarbonView
from ui.Animation import Animation
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
        if self.moleculeIsValid():
            self.checkGuess()

    def clearMolecule(self):
        self.view.clearImages()
        self.molecule = None
        self.ui.informationText.setPlainText("")
        self.ui.nomenclatureBox.setPlainText("")
        self.ui.guessResultLabel.setVisible(False)

    def moleculeIsValid(self):
        carbonMatrix = self.view.getCarbonMatrix()
        alertUser = self.ui.nomenclatureBox.setPlainText
        try:
            self.molecule = Alkane(carbonMatrix)
            return True
        #Raised when no carbons were added in the draw view
        except EmptyAlkaneError:
            alertUser("Please click in the grid to add carbons")
            return False
        #Raised when there are loops and blocks in the molecule
        except CyclicAlkaneError:
            alertUser("The molecule contains a loop or a block.")
            return False
        #Raised when not all of the carbons are adjacent
        except AlkaneNotConnectedError:
            alertUser("Not all of the carbons are connected.")
            return False
        #Raised on malformed substituents
        except BranchingCarbonChainError:
            alertUser("Only straight-chain substituents are supported.")
            return False
        #Raised on molecules with chains that are too long
        except LongestChainTooLongError:
            alertUser("This molecule is too large for me to name.")
            return False
        #Raised on molecules with substituents that are too long
        except SubstituentTooLargeError:
            alertUser("This molecule has a substituent that is too long.")
            return False
        #Raised on molecules with too many of one type of substituent
        except TooManyOfOneSubstituentGroupError:
            alertUser("This molecule has too many of one kind of substituent.")
            return False
    

    def getName(self):
        if self.moleculeIsValid():
            self.ui.nomenclatureBox.setPlainText(self.molecule.name)

    def checkGuess(self):
        self.ui.guessResultLabel.setVisible(True)
        if self.molecule.verify(self.ui.nomenclatureBox.toPlainText()):
            self.ui.guessResultLabel.setText("Correct!")
        else:
            self.ui.guessResultLabel.setText("Incorrect")

    def renderAlkane(self):
        self.view.setScreenToAlkane(self.molecule)
        
    def makeRandom(self):
        self.clearMolecule()
        self.molecule = Alkane.createRandomAlkane()
        self.view.setScreenToAlkane(self.molecule)

    def animate(self):
        self.view.clearImages()
        self.view.passAlkane(self.molecule)

    def getWebInfo(self):
        if self.moleculeIsValid():
            self.ui.nomenclatureBox.setPlainText(self.molecule.name)
            try:
                webMolecule = chemspipy.find_one(self.molecule.name)
                if webMolecule:
                    webMolecule.loadextendedcompoundinfo()
                    infoString = "Common Name: " + str(webMolecule.commonname)
                    infoString += "\nAverage Mass: " + str(webMolecule.averagemass)
                    infoString += "\nMolecular Weight: " + str(webMolecule.molecularweight)
                    infoString += "\nMono Isotopic Mass: " + str(webMolecule.monoisotopicmass)
                    infoString += "\nNominal Mass: " + str(webMolecule.nominalmass)
                else:
                    infoString = "Molecule not found"
            except:
                infoString = "Could not connect to remote service."
            
            self.ui.informationText.setPlainText(infoString)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()

    myapp.show()
    sys.exit(app.exec_())