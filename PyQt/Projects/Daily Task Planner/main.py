import sqlite3

from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('main.ui', self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)

    def calendarDateChanged(self):
        print("Calendar date changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print(dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.taskslistWidget.clear()
        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        query =  "SELECT task, completed FROM tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall()
        print(results)
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked if result[1] == "NO" else QtCore.Qt.Checked)
            self.taskslistWidget.addItem(item)

    def saveChanges(self):
        db = sqlite3.connect('data.db')
        cursor = db.cursor()

        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.taskslistWidget.count()):
            item = self.taskslistWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)

        db.commit()

        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setText("Changes saved")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec_()

    def addNewTask(self):
        newTask = str(self.taskLineEdit.text())
        if newTask == "":
            messageBox = QMessageBox()
            messageBox.setIcon(QMessageBox.Information)
            messageBox.setText("Proszę uzupełnić pole")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec_()
        else:
            date = self.calendarWidget.selectedDate().toPyDate()

            db = sqlite3.connect('data.db')
            cursor = db.cursor()

            query = "INSERT INTO tasks (task, completed, date) VALUES (?, ?, ?)"
            row = (newTask, "NO", date,)

            cursor.execute(query, row)
            db.commit()

            self.taskLineEdit.setText("")
            self.updateTaskList(date)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
