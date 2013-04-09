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

        #function bindings
        QtCore.QObject.connect(self.ui.generateButton,QtCore.SIGNAL("clicked()"),self.generate)

    def generate(self):
        #target = Alkane(self.ui.inchiBox.toPlainText())
        print(str(self.ui.inchiBox.toPlainText()))
        pass

    def makeCarbon(self):
        pass

class View(QtGui.QGraphicsView):
    def __init__(self,parent):
        QtGui.QGraphicsView.__init__(self,parent)

        self.setScene(QtGui.QGraphicsScene(self))
        # Okay. This is messy but works for now.
        # Alternatively, would be good to find a way to inherit parent.size()
        self.setSceneRect(QtCore.QRectF(0,0,parent.width(),parent.height()))

        self.pix = QtGui.QPixmap('carbon.png')

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            position = QtCore.QPointF(self.mapToScene(event.pos()))
            print('left-clicked at (%d, %d)' % (position.x(), position.y()))
            self.scene().addPixmap(self.pix)

            #self._start = event.pos()
        else:
            print('right-clicked')
            #self._start = event.pos()

    def mouseReleaseEvent(self,event):
        #start = QtCore.QPointF(self.mapToScene(self._start))
        #end = QtCore.QPointF(self.mapToScene(event.pos()))
        #self.scene().addItem(QtGui.QGraphicsLineItem(QtCore.QLineF(start,end)))
        #for point in (start,end):
            #text = self.scene().addSimpleText('(%d, %d)' % (point.x(), point.y()))
            #text.setBrush(QtCore.Qt.red)
            #text.setPos(point)
        pass


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.target = Alkane('CC')

    myapp.show()
    sys.exit(app.exec_())