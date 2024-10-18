import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import sqlite3

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("tabletutorial.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setHorizontalHeaderLabels(["City", "Country", "Subcountry"])
        self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("data.sqlite")
        cursor = connection.cursor()
        sqlquery = "SELECT * FROM worldcities LIMIT 50"

        i = 0
        self.tableWidget.setRowCount(50)
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row[2])))
            i += 1


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