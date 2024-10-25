from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtCore


tasks = ["Napisać emaila", "Obejrzeć film", "Zadzwonić do mamy"]

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('main.ui', self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.updateTaskList()

    def calendarDateChanged(self):
        print("Calendar date changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate().strftime('%d.%m.%Y')
        print(dateSelected)

    def updateTaskList(self):
        for task in tasks:
            # add to the list widget
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.taskslistWidget.addItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
