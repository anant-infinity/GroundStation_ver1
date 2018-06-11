import sys
import serial
from time import sleep
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

        self.label = QtGui.QLabel(self)
        self.label.resize(100, 50)
        self.label.move(200,200)

        self.command_str = ''
        self.show()

    def close_application(self):
        print("Closed")
        sys.exit()

    def transmit(self):
        text, result = QtGui.QInputDialog.getText(self, "Input Command", "Please Enter Command")
        if result == True:
            self.command_str = str(text)
        print("Transmitting This: ", self.command_str)
        pass

    def recieve(self):
        #Test code for checking working of pyserial with arduino
        # print("Recieving")
        # ser = serial.Serial('/dev/tty.COM1', 9600)  # Establish the connection on a specific port
        # counter = 32  # Below 32 everything in ASCII is gibberish
        #
        # while True:
        #     counter += 1
        #     ser.write(str(chr(counter)))  # Convert the decimal number to ASCII then send it to the Arduino
        #     print(ser.readline())  # Read the newest output from the Arduino
        #     sleep(.1)  # Delay for one tenth of a second
        #     if counter == 255:
        #         counter = 32
        self.label.setText("Received Data is: ") 
        pass


    def getCommandList(self):
        print("List of Commands Are:")
        pass



def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()