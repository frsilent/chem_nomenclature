__author__ = 'rheintze'

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
from chemistry.alkane import Alkane

class Frame():
    
    FRAME_LABELS = ('Initial', 'Highlight Longest Chain', 'Highlight Substituents', 'Highlight Head', 'Show Indices', 'Show Subgroup Names', 'Show Full Name')
    TERMINAL_STRING = "ENDSECTION"
    def __init__(self, label, fileName):
        def __init__(self):
            #The name of this Frame
            self.label = label
            self.items = []
            self.buildFrame()

            self.carbonImage = QtGui.QPixmap('carbon.png').scaled(self.col_width, self.row_height)
            self.HouseImage = QtGui.QPixmap('house.png').scaled(self.col_width, self.row_height)
            self.RoadImage = QtGui.QPixmap('road.png').scaled(self.col_width, self.row_height)
            
            self.description = self.parseInputFromFile(fileName)
    
    
    #Scan the file for a section with a description for our frame
    #If we find one, set our description to that block of the file
    def parseInputFromFile(self, fileName):
        file = open(fileName, 'r')
        #Are we in the section of the file that
        #contains our description?
        inSection = False
        #A list of lines for our description
        description = []
        for line in file:
            if line == self.label:
                inSection = True
                continue
            if inSection:
                #Have we reached the end of our section?
                if line == Frame.TERMINAL_STRING:
                    #Then stop reading the file
                    break
                #We still have description to read
                else:
                    #Append this line of the file to our description
                    description.append(line)
        #Return the description with newlines in tact
        return "\n".join(description)
            

    def getDescription(self):
        return self.description

    def getDrawables(self):
        return self.items
