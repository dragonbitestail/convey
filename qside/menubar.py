from PySide6.QtWidgets import QMenuBar, QMenu, QFileDialog
from PySide6.QtGui import QPixmap


class MenuBar(QMenuBar):
    """Our MenuBar class
    """

    def __init__(self, window=None):
        super().__init__(parent=window)

        #self.mb = window.menuBar()
        self.window = window
        self.menus = {}


    def add_menu(self, name=None):
        menu = QMenu(name)

        self.addMenu(menu)

        # Register our menu in menus for our MenuBar
        self.menus[name] = menu

        return menu

    def add_menu_action(self, menu, action):
        # TODO: Guard aganst add_menu_action where menu does not exist
        self.menus[menu].addAction(action)
