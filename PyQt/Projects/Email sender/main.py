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
        recipient = self.lineEdit.text()
        email_content = self.textEdit.toPlainText()

        if not recipient or not email_content:
            print("Recipient or email content is empty")
            return

        print("Attempting to send email")
        send_email(recipient=recipient, email=email_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()