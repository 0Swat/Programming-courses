from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('main.ui', self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)

    def calendarDateChanged(self):
        print("Calendar date changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate().strftime('%d.%m.%Y')
        print(dateSelected)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
