from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget


class Color(QWidget):


    def __init__(self, rgba=(0, 0, 0, 255), name=None):
        super().__init__()
        if name is not None:
            self.qcolor = QColor(name)
        else:
            self.qcolor = QColor(rgba[0], rgba[1], rgba[2], rgba[3])

        self._set_color()


    def _set_color(self):
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, self.qcolor)
        self.setPalette(palette)
