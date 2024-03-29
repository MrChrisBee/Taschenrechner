import string
import sys
import tkinter as tk
from math import sqrt


class Calculator(tk.Tk):
    def __init__(self, title: str, text: list, code: list, rows: int, cols: int) -> None:
        # create window instance
        super().__init__()
        if len(code) != len(text):
            print(f"Text- and code-list has to be the same size")
            exit(-1)
        elif rows * cols != len(text):
            print(f"Can't create a keybord with \n {len(text)} keys on a {rows}*{cols} grid.")
            exit(-1)
        else:
            self.resizable(False, False)
            self.title(title)
            self.value = 0  # this should be on the screen
            self.operator = ""  # actual operator
            self.chain = ""  # this will be evaluated
            self.display_digits = 18
            self.content = tk.StringVar()
            self.padding = {'padx': 2, 'pady': 10}
            for r in range(rows):
                self.columnconfigure(r, weight=1)

            for c in range(cols):
                self.rowconfigure(c, weight=1)

            for num, (text, action) in enumerate(zip(text, code)):
                # print(num, num // rows, num % rows, num // cols, num % cols, "#", text )
                self.add_button((num // rows) + 1, num % rows, text, action)

            self.do_bindings()
            self.create_display()
            self.set_display('0')

    def do_bindings(self):
        # Todo bind to the right keys
        self.bind('<Escape>', lambda _: sys.exit())
        self.bind('0', lambda _: self.choose_action("0"))
        self.bind('1', lambda _: self.choose_action("1"))
        self.bind('2', lambda _: self.choose_action("2"))
        self.bind('3', lambda _: self.choose_action("3"))
        self.bind('4', lambda _: self.choose_action("4"))
        self.bind('5', lambda _: self.choose_action("5"))
        self.bind('6', lambda _: self.choose_action("6"))
        self.bind('7', lambda _: self.choose_action("7"))
        self.bind('8', lambda _: self.choose_action("8"))
        self.bind('9', lambda _: self.choose_action("9"))

    def create_display(self):
        # todo picture on button in grid
        # learn tkinter
        # pixel = PhotoImage(width=100, height=15)

        tk.Label(self,
                 textvariable=self.content,
                 font=("Ink Free", 12, "bold"),
                 # image=pixel,
                 height=1,
                 width=self.display_digits,
                 compound=tk.CENTER,
                 **self.padding,
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
        # todo check this
        elif len(txt) <= self.display_digits - 4:
            self.content.set(self.content.get() + what)
            self.update()
        # todo what to do if the user types more then 10 digits? nothing?
        # fix or kill me

    def set_display(self, what: str):
        self.content.set(what)

    def add_button(self, _row: int, _col: int, _str: str, _code: str):
        # put text and picture on a frame
        # put the frame on the button
        # place the button on the grid
        # pixel = tk.PhotoImage("biene.png")
        # photoimage = pixel.resize(20, 20)
        act_button = tk.Button(self,
                               text=_str,
                               # image=photoimage,
                               width=2,
                               height=2,
                               compound=tk.LEFT,
                               command=lambda: self.choose_action(_code))
        act_button.grid(row=_row + 1, column=_col, sticky=tk.W)
        self.update()

    def choose_action(self, code):
        on_screen = self.content.get()

        def add_to_chain(param: str):
            self.chain += param

        def divide():
            store_sign("/")

        def times():
            store_sign("*")

        def minus():
            store_sign("-")

        def plus():
            store_sign("+")

        def store_sign(sign):
            self.operator = sign
            add_to_chain(on_screen)
            self.set_display(sign)
            self.value = 0

        def show_value(what: str):
            # keepinmind kim
            # kim if you later got values from display there might be cutted in accuracy
            # check if there has to be decimal

            if float(what) - round(float(what)) == 0:
                self.set_display(f"{float(what):.0f}")
            else:
                self.set_display(f"{float(what):.2f}")

        def reciprocal():
            # works on the value on screen
            # avoid division by zero
            if float(on_screen) != 0:
                show_value(str(1 / float(on_screen)))

        def square_root():
            # works on the value on screen
            # no negative values
            if not on_screen[0] == "-":
                self.set_display(str(sqrt(float(on_screen))))

        def flip_sign():
            # works on the value on screen
            self.set_display(str(float(on_screen) * -1))

        def clear():
            self.set_display("0")
            self.value = 0
            self.chain = ""

        def my_main():
            # valids ~ helper to check fo valid display content
            valids = string.digits + "-."
            # is_sign ~ one char in "+-*/"
            is_sign = on_screen in "+-/*" and len(on_screen) == 1
            # is_value ~ every char of on_screen is valid number
            is_value = not is_sign and \
                       len(list(filter(lambda char: char in valids, on_screen))) == len(on_screen)

            if len(code) > 1:  # only digits got len(code) == 1
                if code == "clear":
                    clear()
                if is_value:
                    if code == "change":
                        flip_sign()
                    elif code == "sqrt":
                        square_root()
                    elif code == "reciprocal":
                        reciprocal()
                    elif code == "plus":
                        plus()
                    elif code == "minus":
                        minus()
                    elif code == "times":
                        times()
                    elif code == "divide":
                        divide()

                if code == "calc":
                    # = pressed
                    if is_value:
                        add_to_chain(on_screen)
                    if not is_sign:  # beware of += or *=
                        # you have to be sure not to evaluate strings with
                        # e.g. + on the end it causes syntax error
                        # when given to eval()
                        # Calculation goes here
                        show_value(str(eval(self.chain)))
                        self.chain = ""
            else:
                if is_value:
                    self.add_to_display(code)
                elif is_sign:
                    add_to_chain(self.operator)
                    self.set_display(code)
            self.update()

        my_main()


def inspect(container):
    for item in container.keys():
        print(f"{item}: {container[item]}")


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

    my_calc = Calculator("Calculation?", txt, code, 4, 5)

    my_calc.mainloop()


if __name__ == '__main__':
    main()
