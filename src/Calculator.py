import tkinter as tk
from math import sqrt


class Calculator(tk.Tk):
    def __init__(self, title) -> None:
        # create window instance
        super().__init__()
        self.title(title)
        self.value = 0
        #self.config(background="#0f0")
        # there is a var self.text_var representing the Display Content
        self.display_txt = tk.StringVar()
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
        pixel = tk.PhotoImage(width=25, height=25)
        padding = {'padx': 5, 'pady': 10}

        tk.Label(self,
                 textvariable=self.display_txt,
                 font=("Ink Free", 15, "bold"),
                 image=pixel,
                 height=25,
                 compound=tk.RIGHT,
                 **padding,
                 anchor=tk.E,
                 bg="white",  # Background Color
                 fg="black",  # Foreground Color --> Font Color
                 relief="raised"
                 ).grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
        self.update()

    def add_to_display(self, what: str):
        txt = self.display_txt.get()
        if txt == '0':
            self.display_txt.set(what)
        elif len(txt) <= 10:
            # Reduce the Length of the Display to 10 digits max
            self.display_txt.set(self.display_txt.get() + what)
            self.update()
        # what to do if the user types more then 10 digits? nothing?

    def add_button(self, _row: int, _col: int, _str: str, _code: str):
        pixel = tk.PhotoImage(width=10, height=10)
        act_button = tk.Button(self,
                               text=_str,
                               # image=pixel,  # TODO PixelImage ??
                               width=1,
                               height=1,
                               compound=tk.CENTER,
                               command=lambda: self.choose_action(_code))
        act_button.grid(row=_row, column=_col, sticky=tk.W)
        self.update()

    def choose_action(self, code):
        if len(code) > 1:
            if code == "clear":
                self.display_txt.set("0")
            elif code == "change":
                self.add_to_display(str(self.display_txt.get()*-1))
            elif code == "sqrt":
                value = sqrt(float(self.display_txt.get()))
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
        my_calc.add_button((num // 4)+1, num % 4, text, action)

    my_calc.add_to_display('0')

    my_calc.mainloop()


if __name__ == '__main__':
    main()
