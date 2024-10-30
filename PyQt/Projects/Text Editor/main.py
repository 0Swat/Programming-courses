import os
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('main.ui', self)

        self.current_path = None

        self.actionNew.triggered.connect(self.NewFileFunction)
        self.actionOpen.triggered.connect(self.OpenFunction)
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

    def NewFileFunction(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None

    def OpenFunction(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), 'Text Files (*.txt)')
        if fname[0]:
            self.setWindowTitle(fname[0])
            with open(fname[0], 'r') as f:
                filetext = f.read()
                self.textEdit.setText(filetext)
            self.current_path = fname[0]

    def SaveFunction(self):
        if self.current_path is not None:
            # save changes no dialog
            filetext = self.textEdit.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(filetext)
        else:
            self.SaveAsFunction()

    def SaveAsFunction(self):
        print("Save file as")

    def UndoFunction(self):
        self.textEdit.undo()

    def RedoFunction(self):
        self.textEdit.redo()

    def CopyFunction(self):
        self.textEdit.copy()

    def CutFunction(self):
        self.textEdit.cut()

    def PasteFunction(self):
        self.textEdit.paste()

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
