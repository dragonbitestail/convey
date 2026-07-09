from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage, QPicture
from PySide6.QtCore import QCoreApplication as QCApp
from PIL import Image as PilImage

from io import BytesIO


def file_open(signal):
    print(f"ToolBar > file_open(): clicked with signal {signal}")

    # ';;' to delimit multiple filters
    filter = "Images (*.avif *.jpg *.png)"

    # Static
    dir = '.'
    selected_filter = "Images (*.avif *.jpg *.png)"
    #file_o = QFileDialog.getOpenFileName(self.window, " File dialog ",
    file_o = QFileDialog.getOpenFileName(None, " File dialog ",
                                         dir, filter, selected_filter)

    print(f"Attempting to open: \"{file_o}\"")
    if file_o[0]:
        #pixmap = QPixmap(file_o[0]) # Works w/o Pillow for PNGs not avif

        buffer = BytesIO()
        img = PilImage.open(file_o[0])
        print(f"[INFO] img.node: {img.mode}, img.format: {img.format}")
        #img.show() # loads img as PNG into some Pil builtin UI window
        img.save(buffer, 'PNG')
        #img_png = PilImage.open(buffer)
        buffer.seek(0)
        #img_png.show() # Works
        #print(f"[INFO] img_png.node: {img_png.mode}, img_png.format: {img_png.format}")

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.read())

        QCApp.instance().active_window.canvas_label.setPixmap(pixmap)

        #pict = QPicture()
        #pict.loadFromData(buffer.read())

        #QCApp.instance().active_window.canvas_label.setPicture(pict)

        #self.window.canvas_label.setPixmap(pixmap)
        #self.window.canvas_label.setScaledContents(True)
        #self.resize(pixmap.width(), pixmap.height())
