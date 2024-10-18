import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("qtcrashcourse.ui", self)


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting...")

