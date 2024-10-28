import sys
from turtledemo.fractalcurves import CurvesTurtle

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('main.ui', self)

        self.actionNew.triggered.connect(self.NewFunction)
        self.actionSave.triggered.connect(self.SaveFunction)
        self.actionSave_as.triggered.connect(self.SaveAsFunction)
        self.actionUndo.triggered.connect(self.UndoFunction)
        self.actionRedo.triggered.connect(self.RedoFunction)
        self.actionCopy.triggered.connect(self.CopyFunction)
        self.actionCut.triggered.connect(self.CutFunction)
        self.actionPaste.triggered.connect(self.PasteFunction)
        self.actionSet_Dark_Mode.triggered.connect(self.DarkModeFunction)
        self.actionSet_Light_Mode.triggered.connect(self.LightModeFunction)
        self.actionChange_Font_Size.triggered.connect(self.FontSizeFunction)

    def NewFunction(self):
        print("New file")

    def SaveFunction(self):
        print("Save file")

    def SaveAsFunction(self):
        print("Save file as")

    def UndoFunction(self):
        print("Undo")

    def RedoFunction(self):
        print("Redo")

    def CopyFunction(self):
        print("Copy")

    def CutFunction(self):
        print("Cut")

    def PasteFunction(self):
        print("Paste")

    def DarkModeFunction(self):
        print("Set dark mode")

    def LightModeFunction(self):
        print("Set light mode")

    def FontSizeFunction(self):
        print("Change font size")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
