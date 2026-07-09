from PySide6.QtWidgets import QToolBar, QMenu, QFileDialog
from PySide6.QtGui import QPixmap

from PySide6.QtCore import QSize


class ToolBar(QToolBar):
    """Our ToolBar class
    """

    def __init__(self, window=None, icon_width=32, icon_height=32):
        super().__init__(parent=window)

        self.setIconSize(QSize(icon_width, icon_height))

        self.window = window

        self.groups = { }


    def add_action(self, action, group="root"):
        # TODO: Guard aganst add_menu_action where menu does not exist
        #self.menus[menu].addAction(action)
        self.addAction(action)

        if group not in self.groups:
            self.groups[group] = []

        self.groups[group].append(action)


    # Based on group name return list of actions belong to the group
    def get_group_actions(self, group):

        return self.groups[group]


    def file_open(self, s):
        print(f"ToolBar > file_open(): clicked with signal {s}")

        # ';;' to delimit multiple filters
        filter = "Images (*.avif *.jpg *.png)"

        # Static
        dir = '.'
        selected_filter = "Images (*.avif *.jpg *.png)"
        file_o = QFileDialog.getOpenFileName(self, " File dialog ",
                                             dir, filter, selected_filter)

        print(f"Attempting to open: \"{file_o}\"")
        if file_o[0]:
            pixmap = QPixmap(file_o[0])
            self.window.canvas_label.setPixmap(pixmap)
            self.window.canvas_label.setScaledContents(True)
            self.resize(pixmap.width(), pixmap.height())
