__author__ = 'rheintze'

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
from ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

from Alkane import Alkane

class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = DrawView(self.ui.graphicsView)

        self.target = None

        #function bindings
        QtCore.QObject.connect(self.ui.generateButton,QtCore.SIGNAL("clicked()"),self.generate)
        QtCore.QObject.connect(self.ui.clearButton,QtCore.SIGNAL("clicked()"),self.view.clearCarbons)

    def generate(self):
        pass

    def makeCarbon(self):
        pass

class DrawView(QtGui.QGraphicsView):
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
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
        
        self.setScene(QtGui.QGraphicsScene(self.parent()))
        self.scene = self.scene()
        self.scene.setSceneRect(0,0,600,300)

        #Load and resize image to fit squarely in the grid
        self.carbonImage = QtGui.QPixmap('carbon.png').scaled(self.col_width, self.row_height)
        self.addGridToScene()
        print(self.scene.width(), self.scene.height())
        
    def addGridToScene(self):
        #Set up pen
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        #Draw Horizontal Lines
        for y in range(0, self.num_rows-1): # don't draw the two outside edge lines
            self.scene.addLine(0, (y+1)*self.row_height, self.width, (y+1)*self.row_height, pen)
            if y == self.num_rows-2:
                print((y+1)*self.row_height)
        #Draw Vertical Lines
        for x in range(0, self.num_cols-1): # don't draw the two outside edge lines
            self.scene.addLine((x+1)*self.col_width, 0, (x+1)*self.col_width, self.height, pen)
            if x == self.num_cols-2:
                print((x+1)*self.col_width)
            
    def drawCarbons(self, qp):
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                #Is there a carbon at this logical position to draw?
                if self.carbonMatrix[row][col]:
                    #Get the transformed graphical coordinates
                    coords = logicalToScreen(self, (row, col))
                    #Draw the carbon image at 
                    qp.drawImage(coords[0], coords[1], self.carbonImage)
    
    #Add or remove carbons based on click position and mouse button
    def mousePressEvent(self,event):
        #Convert global QT coordinates to logical coordinates
        x,y = self.screenToLogical(event.pos())
        print("Logical",x,y)
        screen_pos = self.logicalToScreen((x,y))
        print("Screen",screen_pos)
        #Left click to add a carbon
        if event.button() == QtCore.Qt.LeftButton:
            #Is this square empty?
            if not self.carbonMatrix[x][y]:
                #Place a carbon in this square
                self.carbonMatrix[x][y]=self.scene.addPixmap(self.carbonImage)
                #Add carbon image to screen
                self.carbonMatrix[x][y].setOffset(*screen_pos)
        #Right click to remove a carbon
        elif event.button() == QtCore.Qt.RightButton:
            #Is this square filled?
            if self.carbonMatrix[x][y]:
                #Remove the carbon from this square
                self.scene.removeItem(self.carbonMatrix[x][y])
                #Remove carbon image from scene
                self.carbonMatrix[x][y]=None
    
    #Return (x,y) in logical, safe carbonMatrix coordinates    
    def screenToLogical(self, position):
        x = int(position.x()/self.col_width)
        y = int(position.y()/self.row_height)
        #Clamp logical coordinates to logical boundaries
        x = max(x, 0)
        x = min(x, self.num_cols-1)
        
        y = max(y, 0)
        y = min(y, self.num_rows-1)
        
        return (x, y)
    
    #Return (x,y) in top-left corner screen coordinates
    def logicalToScreen(self, tuple):
        return (int(tuple[0]*self.col_width), int(tuple[1]*self.row_height))
    
    def clearCarbons(self):
        #Reset carbonMatrix to remove logical carbons
        self.carbonMatrix = []
        for col in range(0, self.num_cols):
            self.carbonMatrix.append([])
            for row in range(0, self.num_rows):
                self.carbonMatrix[col].append(None)
        #Remove graphical carbons
        for item in self.scene.items():
            if type(item) is QtGui.QGraphicsPixmapItem:
                self.scene.removeItem(item)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.target = Alkane('CC')

    myapp.show()
    sys.exit(app.exec_())