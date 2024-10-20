import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("qtcrashcourse.ui", self)

        # Button
        self.button.clicked.connect(self.button_clicked)

        # Check Box
        self.checkBox.stateChanged.connect(self.checked)

        # Combo Box
        self.comboBox.setVisible(False)
        list_zawod = ["Lekarz", "Policjant", "Strażak", "Informatyk"]
        for job in list_zawod:
            self.comboBox.addItem(job)
        self.comboBox.currentIndexChanged.connect(self.combochanged)

        # Spin Box
        self.spinBox.setMinimum(18)
        self.spinBox.setMaximum(99)
        self.spinBox.valueChanged.connect(self.spinchanged)

    def button_clicked(self):
        output_str = self.name.toPlainText() + " " + self.surname.toPlainText()
        self.name.setReadOnly(True)
        self.surname.setReadOnly(True)
        self.name.setDisabled(True)
        self.surname.setDisabled(True)
        output_str += ", lat " + str(self.spinBox.value())
        if self.checkBox.isChecked():
            output_str += ", jest zatrudniony"
        else:
            output_str += ", nie zatrudniony"
        print(output_str)

    def checked(self):
        if self.checkBox.isChecked():
            self.comboBox.setVisible(True)
        else:
            self.comboBox.setVisible(False)

    def combochanged(self):
        self.outputlabel.setText(self.comboBox.currentText() + " jest wybrany")

    def spinchanged(self):
        print(self.spinBox.value())

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

