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
        # Alternatively, would be good to find a way to inherit parent.size()
        self.setSceneRect(QtCore.QRectF(0,0,parent.width(),parent.height())) #Yes this is bad and I feel bad

        self.pix = QtGui.QPixmap('carbon.png')

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            self.position = self.mapToScene(event.pos())
            print('left-clicked at (%d, %d)' % (self.position.x(), self.position.y()))

            self.scene().addPixmap(self.pix).setPos(self.position)

        elif event.button() == QtCore.Qt.RightButton:
            self.position = self.mapToScene(event.pos())
            print('right-clicked at (%d, %d)' % (self.position.x(), self.position.y()))

            self.scene().removeItem(self.scene().itemAt(self.position))

    def mouseReleaseEvent(self,event):
        pass


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.target = Alkane('CC')

    myapp.show()
    sys.exit(app.exec_())