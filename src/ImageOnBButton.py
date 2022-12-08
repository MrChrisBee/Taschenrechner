# import tkinter as tk
# from tkinter.ttk import *
#
#
# def hallo():
#     print("Hallo")
#
#
# if __name__ == '__main__':
#     # creating tkinter window
#     root = tk.Tk()
#     # Adding widgets to the root window (using a grid layoutmanager)
#     Label(root, text='GeeksforGeeks', font=(
#         'Verdana', 15)).grid(row=0, column=0, columnspan=4, sticky=tk.W)
#     # Creating a photoimage object to use image
#     photo = tk.PhotoImage(file="biene.png")
#
#     photoImage = photo.subsample(3, 3)
#
#     # here, image option is used to
#     # set image on button
#     Button(root, text='Click Me!', image=photoImage, compound=tk.CENTER, command=hallo)\
#         .grid(row=0, column=0, columnspan=4, sticky=tk.W)
#
#     tk.mainloop()


import tkinter as tk
from PIL import Image, ImageTk

def hallo():
    print("Hallo")


if __name__ == '__main__':

    root = tk.Tk()

    # Position text in frame
    tk.Label(root, text='Position image on button', font=("Ink Free", 12, "bold")).pack(side=tk.TOP, padx=5, pady=5)

    # Create a photoimage object of the image in the path
    photo = tk.PhotoImage(file="biene.png")

    # Resize image to fit on button
    photoimage = photo.subsample(1, 2)

    # Position image on button
    tk.Button(root, image=photoimage, text="110", compound=tk.RIGHT, command=hallo).pack(side=tk.TOP, pady=15)
    tk.mainloop()
