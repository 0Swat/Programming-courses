from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from sidebar import MySideBar
import sys

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec_()