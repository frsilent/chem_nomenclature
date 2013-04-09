__author__ = 'rheintze'

import sys
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow #pulls from ui.py which can be created from .ui xml file using the pyuic tool

from Alkane import Alkane

class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = View(self.ui.graphicsView)
        self.target = None

        QtCore.QObject.connect(self.ui.generateButton,QtCore.SIGNAL("clicked()"),self.generate)

    def generate(self):
        #target = Alkane(self.ui.inchiBox.toPlainText())
        print(str(self.ui.inchiBox.toPlainText()))
    def makeCarbon(self):
        pass

class View(QtGui.QGraphicsView):
    def __init__(self,parent):
        QtGui.QGraphicsView.__init__(self,parent)
        #TODO: This needs to be restructed so that the scene inherits the view from the graphicsview object
        self.setScene(QtGui.QGraphicsScene(self)) #Particularly this line needs to be sized right
        print(self.viewport().rect())
        #self.setSceneRect(QtGui.QGraphicsView.sceneRect())
        self.setSceneRect(QtCore.QRectF(self.viewport().rect())) #this adds box for me to draw in; kewl

    def mousePressEvent(self,event):
        self._start = event.pos()
    def mouseReleaseEvent(self,event):
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(event.pos()))
        self.scene().addItem(QtGui.QGraphicsLineItem(QtCore.QLineF(start,end)))
        for point in (start,end):
            text = self.scene().addSimpleText('(%d, %d)' % (point.x(), point.y()))
            text.setBrush(QtCore.Qt.red)
            text.setPos(point)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.target = Alkane('CC')

    myapp.show()
    sys.exit(app.exec_())