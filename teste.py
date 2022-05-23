from tkinter import Tk, Scale, TOP, VERTICAL, LEFT, RIGHT, END, DISABLED, NORMAL, Entry, Label
from tkinter import IntVar, Radiobutton, Checkbutton, Canvas, Frame, Menu, Text, Button, PhotoImage, messagebox, ttk

colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

r = 0
for c in colours:
    Label(text=c, relief=RIDGE, width=15).grid(row=r, column=0)
    Entry(bg=c, relief=SUNKEN, width=10).grid(row=r, column=1)
    r = r + 1
