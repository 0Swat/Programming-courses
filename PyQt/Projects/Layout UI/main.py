from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('main.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
