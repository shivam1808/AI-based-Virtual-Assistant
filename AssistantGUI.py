from PyQt5 import QtCore, QtGui, QtWidgets
from process_module import process
from output_module import output
import assistant_details

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 613)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background: url(85e8fb5bd7897610782929cd285c7c33.jpg)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 231, 31)) 
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 470, 471, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setStyleSheet("background: rgb(255, 255, 255)")
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit.setObjectName("textEdit")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font_button = QtGui.QFont()
        font_button.setFamily("Algerian")
        font_button.setPointSize(10)
        font_button.setBold(True)
        font_button.setWeight(10)

        self.pushButton.setFont(font_button)
        self.pushButton.setGeometry(QtCore.QRect(490, 470, 51, 41))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setStyleSheet('QPushButton {background-color: #000000; color: white; background-image: url(speak.jpg);}')
        self.pushButton.setStyleSheet('QPushButton::hover { background-color : white; background-image: url(speak.jpg); color: black;}')
        self.pushButton.setText("Speak")
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setAutoRepeatDelay(299)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setFont(font_button)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 470, 51, 41))
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #000000; color: white; background-image: url(mic2.jpg);}')
        self.pushButton_2.setStyleSheet('QPushButton::hover { background-color : white; background-image: url(mic2.jpg); color: black;}')
        self.pushButton_2.setText("Mic")
        self.pushButton_2.setAutoRepeat(True)
        self.pushButton_2.setAutoRepeatDelay(299)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setFont(font_button)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 520, 111, 51))
        self.pushButton_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_3.setStyleSheet('QPushButton {background-color: #000000; color: white; background-image: url(send.png);}')
        self.pushButton_2.setStyleSheet('QPushButton::hover { background-color : white; background-image: url(send.png); color: black;}')
        self.pushButton_3.setText("Send")
        self.pushButton_3.setAutoRepeat(True)
        self.pushButton_3.setAutoRepeatDelay(299)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.input_fun)

        font_body = QtGui.QFont()
        font_body.setFamily("MS Sans Serif")
        font_body.setPointSize(15)
        font_body.setBold(True)
        font_body.setWeight(10)

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 50, 591, 411))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(font_body)
        self.textEdit_2.setStyleSheet('color: white;')

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def input_fun(self): 
        mytext = self.textEdit.toPlainText() 
        self.textEdit_2.append("Me: " + mytext)
        self.textEdit.setText("")
        res = process(mytext)
        self.textEdit_2.append(assistant_details.name + ": " + res)
        self.textEdit_2.append("")        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Virtual Assistant</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

