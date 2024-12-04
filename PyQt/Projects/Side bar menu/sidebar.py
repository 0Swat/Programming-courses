from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
import resource_rc

class MySideBar(QMainWindow):
    def __init__(self):
        super(MySideBar, self).__init__()
        loadUi("sidebar.ui", self)
        self.setWindowTitle("SideBar Menu")

        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        self.profile_1.clicked.connect(self.switch_to_profilePage)
        self.profile_2.clicked.connect(self.switch_to_profilePage)

        self.messeges_1.clicked.connect(self.switch_to_messegesPage)
        self.messeges_2.clicked.connect(self.switch_to_messegesPage)

        self.notifications_1.clicked.connect(self.switch_to_notificationsPage)
        self.notifications_2.clicked.connect(self.switch_to_notificationsPage)

        self.settings_1.clicked.connect(self.switch_to_settingsPage)
        self.settings_2.clicked.connect(self.switch_to_settingsPage)

    def switch_to_dashboardPage(self):
        self.header_widget.setCurrentIndex(0)

    def switch_to_profilePage(self):
        self.header_widget.setCurrentIndex(1)

    def switch_to_messegesPage(self):
        self.header_widget.setCurrentIndex(2)

    def switch_to_notificationsPage(self):
        self.header_widget.setCurrentIndex(3)

    def switch_to_settingsPage(self):
        self.header_widget.setCurrentIndex(4)