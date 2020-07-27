import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class Chat(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.populateUI()

        self.resize(400, 400)
        self.center()
        self.setWindowTitle('Simple Chat')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def populateUI(self):
        self.createMenu()
        self.statusBar()
        centralWidget = CentralWidget()
        self.setCentralWidget(centralWidget)

    def createMenu(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(self.createExitAction())

        helpMenu = menuBar.addMenu('&Help')
        helpMenu.addAction(self.createAboutAction())

    def createExitAction(self):
        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        return exitAction

    def createAboutAction(self):
        aboutAction = QtWidgets.QAction(QtGui.QIcon('info.png'), '&About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.setStatusTip('Information about the program')
        aboutAction.triggered.connect(self.createAboutDialog)
        return aboutAction

    def createAboutDialog(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle('About')
        dialog.setWindowIcon(QtGui.QIcon('info.png'))
        dialog.resize(200, 200)
        dialog.exec_()

class CentralWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ribbon = QtWidgets.QTextEdit()
        chat = QtWidgets.QTextEdit()
        sendBtn = QtWidgets.QPushButton('Send')

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(3)
        grid.addWidget(ribbon, 0, 0, 1, 3)
        grid.addWidget(chat, 1, 0, 1, 1)
        grid.addWidget(sendBtn, 1, 2)

        self.setLayout(grid)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    chat = Chat()
    sys.exit(app.exec_())