import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from emoji import emojize
import socket
import threading

IsFirstTimeOpened = True
USERNAME = ''
UDP_MAX_SIZE = 65535
Emoji = ''


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
        MainWindow.resize(990, 657)
        MainWindow.setMaximumSize(QtCore.QSize(990, 657))
        MainWindow.setStyleSheet("background-color: rgb(231, 255, 232);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 70, 991, 501))
        self.listWidget.setMinimumSize(QtCore.QSize(991, 501))
        self.listWidget.setStyleSheet("background-color: rgb(231, 255, 232);\n"
                                      "font: 12pt \"MS Sans Serif\";")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 580, 1001, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButton.setStyleSheet("background-color: rgb(252, 255, 39);")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.sendMessageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendMessageButton.setStyleSheet("background-color: rgb(148, 255, 166);")
        self.sendMessageButton.setObjectName("sendMessageButton")
        self.horizontalLayout.addWidget(self.sendMessageButton)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 991, 81))
        self.frame.setStyleSheet("background-color: rgb(105, 255, 5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(820, 20, 151, 41))
        self.titleLabel.setStyleSheet("font: 22pt \"Comic Sans MS\";")
        self.titleLabel.setObjectName("titleLabel")
        self.userLabel = QtWidgets.QLabel(self.frame)
        self.userLabel.setGeometry(QtCore.QRect(10, 30, 661, 31))
        self.userLabel.setStyleSheet("font: 18pt \"Comic Sans MS\";")
        self.userLabel.setObjectName("userLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 570, 991, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SCOOPy"))
        self.toolButton.setText(_translate("MainWindow", ":)"))
        self.sendMessageButton.setText(_translate("MainWindow", "SEND"))
        self.titleLabel.setText(_translate("MainWindow", "SCOOPy"))
        self.userLabel.setText(_translate("MainWindow", "USER"))


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


class Ui_Dialog_Emoji(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(153, 206)
        Dialog.setMinimumSize(QtCore.QSize(153, 0))
        Dialog.setMaximumSize(QtCore.QSize(246, 206))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 51, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 10, 51, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))
        self.pushButton_5.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_10.setText(_translate("Dialog", "PushButton"))
        self.pushButton_12.setText(_translate("Dialog", "PushButton"))
        self.pushButton_13.setText(_translate("Dialog", "PushButton"))
        self.pushButton_11.setText(_translate("Dialog", "PushButton"))
        self.pushButton_6.setText(_translate("Dialog", "PushButton"))


class EmojiDialog(QtWidgets.QDialog, Ui_Dialog_Emoji):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitEmoji()

    def InitEmoji(self):
        self.pushButton.setText(emojize(":smiling_face_with_sunglasses:"))
        self.pushButton_2.setText(emojize(":grinning_face:"))
        self.pushButton_3.setText(emojize(":loudly_crying_face:"))
        self.pushButton_4.setText(emojize(":rolling_on_the_floor_laughing:"))
        self.pushButton_5.setText(emojize(":face_with_tears_of_joy:"))
        self.pushButton_6.setText(emojize(":slightly_smiling_face:"))
        self.pushButton_10.setText(emojize(":smiling_face_with_halo:"))
        self.pushButton_11.setText(emojize(":angry_face:"))
        self.pushButton_12.setText(emojize(":zipper-mouth_face:"))
        self.pushButton_13.setText(emojize(":unamused_face:"))

        self.pushButton.clicked.connect(self.returnEmoji)
        self.pushButton_2.clicked.connect(self.returnEmoji)
        self.pushButton_3.clicked.connect(self.returnEmoji)
        self.pushButton_4.clicked.connect(self.returnEmoji)
        self.pushButton_5.clicked.connect(self.returnEmoji)
        self.pushButton_6.clicked.connect(self.returnEmoji)
        self.pushButton_10.clicked.connect(self.returnEmoji)
        self.pushButton_11.clicked.connect(self.returnEmoji)
        self.pushButton_12.clicked.connect(self.returnEmoji)
        self.pushButton_13.clicked.connect(self.returnEmoji)

    def returnEmoji(self):
        global Emoji
        if self.sender().text() != ':)' and self.sender().text():
            Emoji += self.sender().text()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = ''
        self.InitUI()
        self.connect_to_server('localhost', 3001)
        self.listen()

    def connect_to_server(self, host: str, port: int) -> None:
        self.host, self.port = host, port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((self.host, self.port))
        self.sock.send(f'__join{self.name}'.encode('utf-8'))

    def listen(self):
        threading.Thread(target=self.receiveMessages, daemon=True).start()

    def InitUI(self):
        global IsFirstTimeOpened
        if IsFirstTimeOpened:
            dial = Dialog()
            IsFirstTimeOpened = False
            dial.show()
            dial.exec_()

        self.setName()
        self.userLabel.setText(self.name)
        self.toolButton.clicked.connect(self.chooseEmoji)
        self.sendMessageButton.clicked.connect(self.sendMessages)

    def chooseEmoji(self):
        global Emoji
        emoji = EmojiDialog()
        emoji.show()
        emoji.exec_()
        self.lineEdit.setText(self.lineEdit.text() + Emoji)
        Emoji = ''

    def setName(self):
        global USERNAME
        self.name = USERNAME

    def sendMessages(self):
        message = self.lineEdit.text()
        if message:
            self.sock.send(f'{self.name}: {message}'.encode('utf-8'))
            self.listWidget.addItem('вы: ' + message)
            self.lineEdit.setText('')
            return message
        else:
            return

    def receiveMessages(self):
        while True:
            msg = self.sock.recv(UDP_MAX_SIZE)
            self.listWidget.addItem(str(msg.decode('utf-8')))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
