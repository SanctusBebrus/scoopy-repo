import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
import speech_recognition

IsFirstTimeOpened = True
USERNAME = ''
UDP_MAX_SIZE = 65535


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

        self.voice_to_text_button = QtWidgets.QPushButton('voice text', self)
        self.voice_to_text_button.setGeometry(926, 620, 65, 20)
        self.voice_to_text_button.setStyleSheet("background-color: green")
        self.voice_to_text_button.clicked.connect(self.btn_clicked)

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


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = ''
        self.InitUI()
        self.connect_to_server('localhost', 3001)
        self.listen()
        self.voice_recognizer = speech_recognition.Recognizer()

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

        self.sendMessageButton.clicked.connect(self.sendMessages)

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
            print(str(msg.decode('utf-8')))
            self.listWidget.addItem(str(msg.decode('utf-8')))

    def voice_to_text(self) -> str:
        try:
            with speech_recognition.Microphone(device_index=1) as source:
                self.voice_recognizer.adjust_for_ambient_noise(source)
                print('пытаюсь услышать')
                audio = self.voice_recognizer.listen(source)
            text = self.voice_recognizer.recognize_google(audio, language='ru-RU').lower()
        except Exception:
            return ''
        return text

    def change_voicebtn_color(self, color: str) -> None:
        self.voice_to_text_button.setStyleSheet(f"background-color: {color}")

    def voice_btn_pushed_thread(self):
        self.change_voicebtn_color('red')
        text = self.voice_to_text()
        self.lineEdit.setText(text)
        self.change_voicebtn_color('green')

    def btn_clicked(self):
        threading.Thread(target=self.voice_btn_pushed_thread).start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
