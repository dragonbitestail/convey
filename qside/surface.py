from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtCore import QCoreApplication as QCApp

class Canvas(QtWidgets.QLabel):

    def __init__(self, parent=None, tool=None):
        super().__init__(parent=parent)

        # Initial size
        pixmap = QtGui.QPixmap(1200, 600)
        pixmap.fill(Qt.gray)

        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None

        if tool is None:
            self.pen_color = QtGui.QColor(255, 255, 0, a=17)
            self.pen_width = 9

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        pos = e.position()
        if self.last_x is None: # First event.
            self.last_x = pos.x()
            self.last_y = pos.y()
            return # Ignore the first time.

        canvas = QCApp.instance().active_window.canvas_label.pixmap()
        painter = QtGui.QPainter(
            canvas
        )
        #painter.setOpacity(0.5)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)

        p = painter.pen()
        p.setWidth(self.pen_width)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, pos.x(), pos.y())
        painter.end()

        QCApp.instance().active_window.canvas_label.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = pos.x()
        self.last_y = pos.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    #def paintEvent(self, e):
    #    print(f"paintEvent(): w/ e = {e}")
