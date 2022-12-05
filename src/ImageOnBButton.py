from tkinter import *
from tkinter.ttk import *


def hallo():
    print("Hallo")
# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text='GeeksforGeeks', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
photo = PhotoImage(file="biene.png")

photoImage = photo.subsample(3, 3)

# here, image option is used to
# set image on button
Button(root, text='Click Me !', image=photoImage, compound=LEFT, command=hallo).pack(side=TOP)

mainloop()
