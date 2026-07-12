#!/usr/bin/env python

import argparse
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QLabel, QStackedLayout, QVBoxLayout)

from PySide6.QtCore import Qt

import qside.action_function as AF
import qside.menubar as MB
import qside.toolbar as TB
import qside.surface as SF
import qside.tool as TL
from qside.action import Action
# PySide.QtCore.QCoreApplication.instance()

# When you want to pass command line args on to your app
import sys

class PSideApp(QApplication):


    def __init__(self, *, args=sys.argv):
        super().__init__()

        # Look for opts to indicate we should get image from clipboard
        parser = argparse.ArgumentParser(
            prog='convey',
            description='An image annotation tool'
        )
        parser.add_argument("-c", "--copy", help="Copy image from clipboard",
                            action='store_true')
        args = parser.parse_args()

        # When declaring both short and long form of an argument, only long
        # form is stored in resulting namespace.
        if args.copy:
            self.use_clipboard = True


# PSideApp instance can be reached w/ PySide.QtCore.QCoreApplication.instance()
class MainWindow(QMainWindow):
    def __init__(self, title="My App"):
        super().__init__()

        self.setWindowTitle(title)

        self.config_win = ConfigWindow(title='Tool Configuration')

        # Setup Menubar and Items
        menubar = MB.MenuBar(window=self)
        self.setMenuBar(menubar)

        self.menuBar().add_menu(name='&File')
        self.menuBar().add_menu(name='&Edit')
        menu_view = self.menuBar().add_menu(name='&View')
        #   Submenu Zoom for &View
        menu_view.addMenu('&Zoom')

        self.menuBar().add_menu(name='&Help')

        # Toolbar
        self.toolbar = TB.ToolBar(window=self, icon_width=48, icon_height=48)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)


        # *** Actions ***



        act_file_open = Action(action_name="&Open", func=AF.file_open,
                               parent=self)

        act_file_exit = Action(action_name="&Exit", func=self.close, parent=self)

        # *** Actions -- Toolbar ***
        act_config = Action(icon="./icon/gear.png",
                                 action_name="tool_config", func=TL.config,
                                 parent=self)


        act_highlighter = Action(icon="./icon/highlighter.png",
                                 action_name="highlighter", func=TL.highlighter,
                                 parent=self)
        act_highlighter.setCheckable(True)

        #act_pen = Action("optional arg1 to func", icon="./icon/pen.png",
        act_pen = Action(icon="./icon/pen.png",
                                 action_name="pen", func=TL.pen,
                                 parent=self)
        act_pen.setCheckable(True)

        act_text = Action(icon="./icon/text.png",
                                 action_name="text", func=TL.text,
                                 parent=self)
        act_text.setCheckable(True)


        # WIRE Actions to appropriate controls:
        self.menuBar().add_menu_action(menu="&File", action=act_file_open)
        self.menuBar().add_menu_action(menu="&File", action=act_file_exit)

        self.toolbar.add_action(action=act_config)

        self.toolbar.add_action(action=act_highlighter)
        self.toolbar.add_action(action=act_pen)
        self.toolbar.add_action(action=act_text)

        # ---------- Canvas and Interface Setup -------------
        # Our canvas label use as target of our images:
        # Images may be manually load use menubar > File > Open's action
        # Future method will include opening image at app start and grabbing
        # from clipboard when appropriate command-line arg. is passed.
        #self.canvas_label = QLabel(self)
        self.canvas_label = SF.Canvas(parent=self)

        layout = QStackedLayout()

        layout.addWidget(self.canvas_label)
        print(f"canvas_label added at index: {layout.currentIndex()}")

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


class ConfigWindow(QWidget):
    def __init__(self, title="My App"):
        super().__init__()

        self.setWindowTitle(title)
        layout = QVBoxLayout()
        self.label = QLabel("Config Window for a currently selected Tool")
        layout.addWidget(self.label)
        self.setLayout(layout)


def main():
    # Root of your UI App
    app = PSideApp(args=sys.argv)

    # Create a Qt widget, which will be our window.
    window = MainWindow('Convey')

    window.show()  # Windows are hidden by default.

    # Start the event loop.
    app.exec()


if __name__ == '__main__':
    # main() > PSideApp for evaluation & storage of command-line flags and args
	main()
