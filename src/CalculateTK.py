import tkinter as tk
from config.config import ROOT_DIR


class Rechner(tk.Tk):
    # TODO: Add Logging
    # TODO: pimp logic

    def __init__(self, title) -> None:
        # create window instance
        super().__init__()
        self.title(title)
        # self.config(background="#0f0")
        # there is a var self.text_var representing the Display Content
        self.display_txt = tk.StringVar()
        # Use the trace() method of the StringVar object to trace the text changes.
        # self.display_txt.trace('w', self.zugriff())
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        # self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.create_display()

    def create_display(self):
        pixel = tk.PhotoImage(width=25, height=25)
        padding = {'padx': 40, 'pady': 40}

        tk.Label(self,
                 textvariable=self.display_txt,
                 font=("Ink Free", 20, "bold"),
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
        if self.display_txt.get() == '0':
            self.display_txt.set(what)
        else:
            self.display_txt.set(self.display_txt.get() + what)
        self.update()

    def add_button(self, _row: int, _col: int, _str: str, _code: str):
        # what about myaction
        pixel = tk.PhotoImage(width=10, height=10)
        # TODO: Could a Button be reduced (closure) to ?.but_num(2) and ?.but_com("+")
        act_button = tk.Button(self,
                               text=_str,
                               # image=pixel,  # TODO PixelImage ??
                               width=1,
                               height=1,
                               compound=tk.CENTER,
                               command=lambda: self.add_to_display(_str))
        act_button.grid(row=_row, column=_col, sticky=tk.W)
        self.update()

def main():
    # TODO: add '<-' 'C' 'sqrt' utf_8('U+221A')
    # build representation of keys with text an code
    txt: list[str] = ['C', '+-', 'sqrt', '1/x',
                      '1', '2', '3', '+',
                      '4', '5', '6', '-',
                      '7', '8', '9', '*',
                      '.', '0', '=', '/']

    code: list[str] = ['clear', 'change', 'sqrt', 'reciprocal',
                       '1', '2', '3', 'plus',
                       '4', '5', '6', 'minus',
                       '7', '8', '9', 'times',
                       '.', '0', 'calc', 'divide']

    my_calc = Rechner("Calculation?")

    for num, (text, action) in enumerate(zip(txt, code)):
        # got 16 buttons make 4 each row, num // 4 is the row
        # num % 4 ist the col, text is label on button
        # code is what to do, add_button(row, col, str, code)
        print(f"Row {(num // 4)+1} Col {num % 4} ")
        my_calc.add_button((num // 4)+1, num % 4, text, action)

    my_calc.add_to_display('0')

    my_calc.mainloop()


if __name__ == '__main__':
    main()
