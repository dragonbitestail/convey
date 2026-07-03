from tkinter import filedialog as fd
from tkinter import Canvas
import tkinter as tk
from PIL import ImageTk, Image


global canvas, x_start, y_start, last_rectangle

canvas = None
last_rectangle = None
canvas_objects = []

def undo_object(event):
    print(f"undo_object: event: {event}")
    if canvas_objects:
        canvas.delete(canvas_objects.pop())

def mouse_1(event):
    global x_start, y_start

    x_start = event.x
    y_start = event.y
    print(f"mouse_1: x_start: {x_start}, y_start: {y_start}")

def drag_stop(event):
    global x_start, y_start

    print(f"drag_stop: {event.x} and {event.y}")
    rectangle = canvas.create_rectangle(x_start, y_start, event.x, event.y,
                                        outline="red", width=4, fill=None)
    canvas_objects.append(rectangle)

    if last_rectangle is not None:
        canvas.delete(last_rectangle)

    canvas.update_idletasks()


def drag_handler(event=None):
    global last_rectangle
    #print(f"{event.x} and {event.y}")

    if last_rectangle is not None:
        canvas.delete(last_rectangle)

    last_rectangle = canvas.create_rectangle(x_start, y_start, event.x, event.y,
                                             outline="red", fill=None)


def file_open(parent):
    global canvas

    # launch file open dialog to get user selected
    # image file
    file_name = fd.askopenfilename(initialdir='~/Desktop',
                                   filetypes=[('avif', '*.avif'),
                                              ('jpg', '*.jpg'),
                                              ('png', '*.png'),
                                              ])

    print(f"selected file_name \"{file_name}\"")

    loaded_img = ImageTk.PhotoImage(Image.open(file_name))

    print((f"Creating Canvas for loaded image: width = "
           f"\"{loaded_img.width()}\", height = \"{loaded_img.height()}\""))

    canvas = Canvas(parent, width=loaded_img.width(),
                    height=loaded_img.height())
    canvas.image = loaded_img # prevents image from getting GC'd by Python
    canvas.create_image(10, 10, anchor=tk.NW,
                        image=loaded_img)

    canvas.pack(fill=tk.BOTH)

    canvas.bind("<Button-1>", mouse_1)
    canvas.bind("<B1-Motion>", drag_handler)
    canvas.bind("<ButtonRelease-1>", drag_stop)

    parent.bind("<Control-z>", undo_object)

    parent.update_idletasks()
    #parent.update()
