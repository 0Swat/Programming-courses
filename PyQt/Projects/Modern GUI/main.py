import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget, QLineEdit
import sqlite3


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('welcomescreen.ui', self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        loginscreen = LoginScreen()
        widget.addWidget(loginscreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocreate(self):
        createscreen = CreateAccScreen()
        widget.addWidget(createscreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        email = self.emailfield.text()
        password = self.passwordfield.text()
        if len(email) == 0 or len(password) == 0:
            self.label_password.setText("Proszę uzupełnić dane")
        else:
            conn = sqlite3.connect('shop_data.db')
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\'' + email + "\'"
            cur.execute(query)
            if cur.fetchone() is None:
                self.label_password.setText("Invalid username or password")
            else:
                cur.execute(query)
                result_pass = cur.fetchone()[0]
                print(result_pass)
                if result_pass == password:
                    print("Successfully logged in.")
                    self.label_password.setText("")
                else:
                    self.label_password.setText("Invalid username or password")

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("create.ui", self)
        self.password_create.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_create_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.gotosignup)

    def gotosignup(self):
        email = self.email_create.text()
        password = self.password_create.text()
        password2 = self.password_create_2.text()
        if email == "" or password == "" or password2 == "":
            self.label_create.setText("Proszę uzupełnić dane.")
        elif password != password2:
            self.label_create.setText("Hasła się nie zgadzają.")
        else:
            conn = sqlite3.connect('shop_data.db')
            cur = conn.cursor()
            query = 'SELECT username FROM login_info WHERE username =\'' + email + "\'"
            cur.execute(query)
            if cur.fetchone() is not None:
                self.label_create.setText("Podany użytkownik już istnieje")
            else:
                cur.execute('INSERT INTO login_info (username, password) VALUES (?, ?)', (email, password))
                conn.commit()
                conn.close()

# main
app = QApplication(sys.argv)
mainwindow = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting...")