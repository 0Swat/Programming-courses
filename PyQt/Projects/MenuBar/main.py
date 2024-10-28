import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('main.ui', self)

        self.actionNew.triggered.connect(self.NewFile)
        self.actionUndo.triggered.connect(self.UndoAction)

    def NewFile(self):
        print('New File')

    def UndoAction(self):
        print('Undo File')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
