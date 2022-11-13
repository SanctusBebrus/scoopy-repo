import sys
from PyQt5 import QtCore, QtGui, QtWidgets

IsFirstTimeOpened = True
USERNAME = ''


def receiveMessage(message):
    print(message)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 183)
        self.userNameLine = QtWidgets.QLineEdit(Dialog)
        self.userNameLine.setGeometry(QtCore.QRect(40, 60, 301, 31))
        self.userNameLine.setObjectName("userNameLine")
        self.askForNameLabel = QtWidgets.QLabel(Dialog)
        self.askForNameLabel.setGeometry(QtCore.QRect(70, 20, 241, 31))
        self.askForNameLabel.setStyleSheet("font: 16pt \"Comic Sans MS\";")
        self.askForNameLabel.setObjectName("askForNameLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 100, 251, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.confirmButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.askForNameLabel.setText(_translate("Dialog", "Как вас называть?"))
        self.confirmButton.setText(_translate("Dialog", "Подтвердить"))
        self.cancelButton.setText(_translate("Dialog", "Отмена"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 70, 881, 431))
        self.listWidget.setObjectName("listWidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(720, 0, 261, 41))
        self.titleLabel.setStyleSheet("font: 22pt \"Comic Sans MS\";")
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 510, 881, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageLine = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.messageLine.setObjectName("messageLine")
        self.horizontalLayout.addWidget(self.messageLine)
        self.sendMessageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendMessageButton.setObjectName("sendMessageButton")
        self.horizontalLayout.addWidget(self.sendMessageButton)
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(10, 10, 661, 31))
        self.userLabel.setStyleSheet("font: 18pt \"Comic Sans MS\";")
        self.userLabel.setObjectName("userLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEST GUI SCOOPy"))
        self.titleLabel.setText(_translate("MainWindow", "SCOOPy BETA"))
        self.sendMessageButton.setText(_translate("MainWindow", "SEND"))
        self.userLabel.setText(_translate("MainWindow", ""))


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitDialog()

    def InitDialog(self):
        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.cancel)

    def confirm(self):
        global USERNAME
        if self.userNameLine.text():
            USERNAME = self.userNameLine.text()
            self.close()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.about(self, 'Ошибка', 'Поле с именем пусто')

    def cancel(self):
        exit()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = ''
        self.InitUI()

    def InitUI(self):
        global IsFirstTimeOpened
        if IsFirstTimeOpened:
            dial = Dialog()
            IsFirstTimeOpened = False
            dial.show()
            dial.exec_()

        self.setName()
        self.userLabel.setText(self.name)

        self.sendMessageButton.clicked.connect(self.sendMessages)

    def setName(self):
        global USERNAME
        self.name = USERNAME

    def sendMessages(self):
        message = self.messageLine.toPlainText()
        if message:
            receiveMessage(message)
            self.listWidget.addItem('вы: ' + message)
            self.messageLine.setText('')
            return message
        else:
            return

    def receiveMessages(self, *message):
        self.listWidget.addItem(str(*message))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
