import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QTreeWidgetItem
from PyQt5.uic import loadUi
import xml.etree.ElementTree as et

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("treewidgettutorial.ui", self)
        f = open("books.xml", 'r').read()
        self.printtree(f)
        self.treeWidget.itemClicked.connect(self.onItemClicked)

    def printtree(self, s):
        tree = et.fromstring(s)
        self.treeWidget.setColumnCount(1)
        a = QTreeWidgetItem([tree.tag])
        self.treeWidget.addTopLevelItem(a)

        def displayTree(a, s):
            for child in s:
                branch = QTreeWidgetItem([child.tag])
                a.addChild(branch)
                displayTree(branch, child)
            if s.text is not None:
                content = s.text
                a.addChild(QTreeWidgetItem([content]))

        displayTree(a, tree)

    def onItemClicked(self):
        item = self.treeWidget.currentItem()
        print(item.text(0))
        print(self.getParentPath(item))

    def getParentPath(self, item):
        def getParent(item, output_string):
            if item.parent() is None:
                return output_string
            output_string = item.parent().text(0) + "/" + output_string
            return getParent(item.parent(), output_string)

        output = getParent(item, item.text(0))
        return output

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