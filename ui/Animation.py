__author__ = 'rheintze'

from PyQt4 import QtCore, QtGui
from Frame import Frame

class Animation():
    
    INPUT_SCRIPT_FILENAME = '../script.txt'
    def __init__(self):
        #Creates list of frames; starting with parent's scene
        self.frameList = []
        self.frameIndex = 0
        for name in Frame.FRAME_LABELS:
            self.frameList.append(Frame(name, Animation.INPUT_SCRIPT_FILENAME))
        

    def advanceFrame(self):
        self.frameIndex+=1
        self.setScene(self.frameList[self.frameIndex])
        