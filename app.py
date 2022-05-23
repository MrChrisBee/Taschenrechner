import os
from pathlib import Path
from xmlrpc.client import Boolean
os.chdir(Path(__file__).parent)
from tkinter import TOP, VERTICAL, LEFT, RIGHT, END, DISABLED, NORMAL
from tkinter import Tk, Scale, IntVar, Radiobutton, Checkbutton, Canvas, Frame
from tkinter import Menu, Text, Button, PhotoImage, messagebox, ttk, Entry, Label


window = Tk()


def main_window():
    # Change title
    window.title("CalculateIt")

    # Change Size
    window.geometry("600x600")  # width x height

    # Change other properties like background
    window.config(
        #  background="red"
        background="#c6ecf7"
    )

    # Change Icon of the window
    icon = PhotoImage(file="./grafik.png")
    window.iconphoto(True, icon)


def button_widget(txt: str, my_cmd: str, r: int, c: int) -> None:

    def click_me(my_cmd):
        print(f"You Typed: {my_cmd}")

    # define a button
    Button(window,
           text=str(txt),
           font=("Ink Free", 20, "bold"),

           bg="yellow",
           fg="black",

           padx=20,
           pady=30,

           command=lambda: click_me(my_cmd),
           # state= ACTIVE, # DISABLED
           ).grid(row=r, column=c)


def main():
    r , c = 0, 0
    main_window()
    my_keys = ("√", "x²", "+/-", "C", "1", "2", "3", "+", "4", "5",
               "6", "-", "7", "8", "9", "*", ",", "0", ".", "/", "=")
    my_str = ("sqrt", "pow2", "sign", "clear", "1", "2", "3", "+", "4", "5",
              "6", "-", "7", "8", "9", "*", ",", "0", ".", "/", "exec")
    for _key in zip(my_keys, my_str):
        r += 1
        c = r % 4
        button_widget(_key, row=r, col=c)

    window.mainloop()


main()
