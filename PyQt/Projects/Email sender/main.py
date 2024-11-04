from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
from email_sender import send_email

class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.SendButtonPushed)

    def SendButtonPushed(self):
        send_email(recipient=self.lineEdit.text(), email=self.textEdit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()