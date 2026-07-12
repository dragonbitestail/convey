from PySide6.QtCore import QCoreApplication as QCApp
from PySide6 import QtGui


class Tool():

    def __init__(self):
        #super().__init__()

        self.last_x, self.last_y = None, None

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)


class ToolHighlighter(Tool):

    def __init__(self):
        super().__init__()


def highlighter(signal):

    print(f"[DEBUG] Tool > highlighter() activated = {signal}")


def pen(signal, *args):

    print(f"[DEBUG] Tool > pen() activated = {signal}, w/ args: {args}")

def text(signal, *args):

    print(f"[DEBUG] Tool > text() activated = {signal}, w/ args: {args}")


def config(signal, *args):

    print(f"[DEBUG] Tool > config() activated = {signal}, w/ args: {args}")
    QCApp.instance().activeWindow().config_win.show()


def todo(signal, *args):

    print(f"[DEBUG] Tool > todo() activated = {signal}, w/ args: {args}")
