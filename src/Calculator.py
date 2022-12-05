import tkinter as tk
from tkinter import TclError, ttk
from math import sqrt


class Calculator(tk.Tk):
    def __init__(self, title) -> None:
        # create window instance
        super().__init__()
        self.resizable(False, False)
        self.title(title)
        self.value = 0
        self.display_digits = 17
        # there is a var self.text_var representing the Display Content
        self.content = tk.StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.create_display()

    def create_display(self):
        # pixel = PhotoImage(width=100, height=15)
        padding = {'padx': 2, 'pady': 10}

        tk.Label(self,
                 textvariable=self.content,
                 font=("Ink Free", 12, "bold"),
                 # image=pixel,
                 height=1,
                 width=self.display_digits,
                 compound=tk.CENTER,
                 **padding,
                 anchor=tk.E,
                 bg="white",  # Background Color
                 fg="black",  # Foreground Color --> Font Color
                 relief="raised"
                 ).grid(row=0, column=0, columnspan=4, sticky=tk.W)
        self.update()

    def add_to_display(self, what: str):
        txt = self.content.get()
        if txt == '0':
            self.content.set(what)
        elif len(txt) <= 10:
            # Reduce the Length of the Display to 10 digits max
            self.content.set(self.content.get() + what)
            self.update()
        # what to do if the user types more then 10 digits? nothing?

    def add_button(self, _row: int, _col: int, _str: str, _code: str):
        # rebuild with FrameLabel or Frame

        pixel = tk.PhotoImage("biene.png")
        # photoimage = pixel.subsample(3, 3)
        act_button = tk.Button(self,
                               text=_str,
                               # image=photoimage,
                               width=2,
                               height=2,
                               compound=tk.LEFT,
                               command=lambda: self.choose_action(_code))
        act_button.grid(row=_row, column=_col, sticky=tk.W)
        self.update()

    def display_shows_value(self):
        if self.content.get() in "+-*/":
            # display shows calc sign, no value
            return False
        else:
            return True

    def choose_action(self, code):
        if len(code) > 1:
            if code == "clear":
                self.content.set("0")
                self.value = 0
            elif code == "change":
                self.add_to_display(str(self.content.get() * -1))
            elif code == "sqrt":
                value = sqrt(float(self.content.get()))
        else:
            self.add_to_display(code)

        self.update()


def main():
    # build representation of keys with text and code
    txt: list[str] = ['C', '+/-', '√', '1/x',
                      '1', '2', '3', '+',
                      '4', '5', '6', '-',
                      '7', '8', '9', '*',
                      '.', '0', '=', '/']

    code: list[str] = ['clear', 'change', 'sqrt', 'reciprocal',
                       '1', '2', '3', 'plus',
                       '4', '5', '6', 'minus',
                       '7', '8', '9', 'times',
                       '.', '0', 'calc', 'divide']

    my_calc = Calculator("Calculation?")

    for num, (text, action) in enumerate(zip(txt, code)):
        # got 16 buttons make 4 each row, num // 4 is the row
        # num % 4 ist the col, text is label on button
        # code is what to do, add_button(row, col, str, code)
        # print(f"Row {(num // 4)+1} Col {num % 4} ")
        my_calc.add_button((num // 4) + 1, num % 4, text, action)

    my_calc.add_to_display('0')

    my_calc.mainloop()


if __name__ == '__main__':
    main()
