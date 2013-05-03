__author__ = 'rheintze'

from PyQt4 import QtCore, QtGui
from Frame import Frame

class AnimateView(QtGui.QGraphicsView):
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)

        #Used to set view size & logically separate it into a grid
        self.width = 600
        self.height = 300
        self.num_rows = 10
        self.num_cols = 20

        #Size of each square
        self.col_width = self.width / self.num_cols
        self.row_height = self.height / self.num_rows

        #2D Array to remember which squares have carbons in them
        self.carbonMatrix = []
        for col in range(0, self.num_cols):
            self.carbonMatrix.append([])
            for row in range(0, self.num_rows):
                self.carbonMatrix[col].append(None)

        #Creates list of frames; starting with parent's scene
        self.frameList = []
        self.frameList.append(Frame(QtGui.QGraphicsScene(self.parent())))
        self.index = 0
        self.setScene(self.frameList[self.index])

        self.scene = self.scene()
        self.scene.setSceneRect(0,0,600,300)

        #Creates next frame; clearing the screen and drawing all carbons again
        #Need to figure out constructor which will make a clean scene
        #Alternatively copy frameList & delete all items in it
        self.frameList.append(Frame(QtGui.QGraphicsScene()))
        self.advanceFrame()


    def advanceFrame(self):
        self.index+=1
        self.setScene(self.frameList[self.index])
        self.scene = self.scene()
        self.scene.setSceneRect(0,0,600,300)

    def passAlkane(self,alkane):
        carbons = alkane.getCarbons()
        print(carbons)