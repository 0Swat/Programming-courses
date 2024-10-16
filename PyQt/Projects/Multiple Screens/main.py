import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("screen1.ui", self)
        self.button_1.clicked.connect(self.gotoScreen2)

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("screen2.ui", self)
        self.button_2.clicked.connect(self.gotoScreen1)

    def gotoScreen1(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()




try:
    sys.exit(app.exec_())
except:
    print("Exiting...")