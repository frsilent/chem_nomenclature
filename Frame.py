__author__ = 'rheintze'

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage

class Frame(QtGui.QGraphicsScene):
    def __init__(self,parent):
        def __init__(self):
            self.info = "This is help text to be displayed in the additional info box"


    def getExplanation(self):
        #This will build a string for the help text based on the molecule state
        return self.info