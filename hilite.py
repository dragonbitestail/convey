#!/usr/bin/env python

from tkinter import *
from PIL import ImageTk, Image

import menubar.file as mb_file

global root
root = Tk()


def setup(title='no title'):
    root.title(title)

    # Our root window size
    # TODO: Determine whether to open this to an initial small
    # size, then expand up to full screen depending on size of image.

    root.geometry("700x700")

    # TODO: Determine layout of tools and other controls vs image display
    # area. E.g., two separate frame, w/ toolbar at top/bottom and image in
    # opposite frame.
    menubar = Menu(root)

    # Menu items:
    menu_file = Menu(menubar, tearoff=0)

    menu_file.add_command(label="Open Image", command=lambda: mb_file.file_open(root))
    menu_file.add_command(label="Exit", command=root.quit)

    menubar.add_cascade(label="File", menu=menu_file)
    root.config(menu=menubar)

    root.config(bg='darkgray')


def main():

    root.mainloop()


if __name__ == '__main__':
    setup(title='HiLite')
    main()
