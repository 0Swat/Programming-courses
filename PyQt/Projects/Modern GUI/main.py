import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('welcomescreen.ui', self)

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