__author__ = 'rheintze'

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
from chemistry.alkane import Alkane

class Frame(QtGui.QGraphicsScene):
    def __init__(self,parent):
        QtGui.QGraphicsScene.__init__(self,parent)
        def __init__(self):
            self.info = "This is help text to be displayed in the additional info box"
            self.type = 'start' #Used to create frames of a larger animation; ie start, intermediary, end
            self.items = []
            self.buildFrame()

            self.carbonImage = QtGui.QPixmap('carbon.png').scaled(self.col_width, self.row_height)
            self.HouseImage = QtGui.QPixmap('house.png').scaled(self.col_width, self.row_height)
            self.RoadImage = QtGui.QPixmap('road.png').scaled(self.col_width, self.row_height)

    def getExplanation(self):
        #This will build a string for the help text based on the molecule state
        return {
            'start':"The first step of the IUPAC naming convention is to find the longest path, note that this is x in our alkane",
            'road':"In our mailman analogy, this is replaced by a road",
        }.get(self.type,"Not a valid frame type")

    def getDrawables(self):
        return self.items

    def buildFrame(self):
        pass