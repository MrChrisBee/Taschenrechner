from tkinter import *
from typing import List, Any

from numpy import column_stack


# 1 create window instance


def add_str(what: str):
    pass


window = Tk()
window.title("TK-Calc")
#  window.geometry("600x600")  # with x height
window.config(
    background="#00f"
)

butt: list[str | Any] = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '=', '/']
actions: list[str | Any] = ['add(1)', 'add(2)', 'add(3)', 'add(+)', 'add(4)', 'add(5)', 'add(6)', 'add(-)', 'add(7)',
                            'add(8)', 'add(9)', 'add(*)', 'add(.)', 'add(0)', 'calculate()', 'add(/)']

for taste, action in zip(butt, actions):
    print(taste, action)


def digits_label():
    # Define the label
    label = Label(window,
                  text="0",
                  font=("Ink Free", 20, "bold"),
                  height=1,
                  width=20,
                  anchor=E,
                  padx=10,  # Padding x
                  pady=10,  # Padding y
                  bg="red",  # Background Color
                  fg="blue"  # Foreground Color --> Font Color
                  )
    # label.pack(pady=20)
    label.grid(row=0, column=0, columnspan=4, sticky=N)


digits_label()
window.mainloop()
