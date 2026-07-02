from tkinter import filedialog as fd
from tkinter import Label
from PIL import ImageTk, Image

def file_open(parent):

    # launch file open dialog to get user selected
    # image file
    file_name = fd.askopenfilename(initialdir='~/Desktop',
                                   filetypes=[('.avif', '*.avif')])

    print(f"selected file_name \"{file_name}\"")

    loaded_img = ImageTk.PhotoImage(Image.open(file_name))

    label = Label(parent, image=loaded_img)

    label.pack()
    parent.mainloop()
