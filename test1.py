import sys
from PyQt4 import QtGui, QtCore, uic

qtCreatorFile = "groundstationapp.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Window(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Window, self).__init__()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_quit.clicked.connect(self.close_application)
        self.btn_transmit.clicked.connect(self.transmit)
        self.btn_receive.clicked.connect(self.recieve)


        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        extractAction2 = QtGui.QAction("&Command List", self)
        extractAction2.setShortcut("Ctrl+H")
        extractAction2.setStatusTip('List of All commands')
        extractAction2.triggered.connect(self.getCommandList)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        fileMenu = mainMenu.addMenu('&Command List')
        fileMenu.addAction(extractAction2)


        self.show()

    def close_application(self):
        print("Closed")
        sys.exit()

    def transmit(self):
        print("Transmitting")
        pass

    def recieve(self):
        print("Recieving")
        pass

    def getCommandList(self):
        print("List of Commands Are:")
        pass



def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()