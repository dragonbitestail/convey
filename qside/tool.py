from PySide6.QtCore import QCoreApplication as QCApp

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

    print(f"[DEBUG] highlighter() activated = {signal}")


def pen(signal, *args):

    print(f"[DEBUG] pen() activated = {signal}, w/ args: {args}")
