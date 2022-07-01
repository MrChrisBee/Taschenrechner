import tkinter as tk


class Rechner(tk.Tk):
    def __init__(self) -> None:
        # create window instance
        super().__init__()
        self.title('myCalcualator')
        self.geometry("400x480")
        self.config(background="#00f")
        self.text_var = tk.StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.create_widgets()

    def create_widgets(self):
        pixel = tk.PhotoImage(width=1, height=1)
        padding = {'padx': 5, 'pady': 1}
        self.text_var.set('0')
        tk.Label(self,
                 textvariable=self.text_var,
                 font=("Ink Free", 20, "bold"),
                 image=pixel,
                 width=400,
                 height=50,
                 compound='c',
                 **padding,
                 anchor=tk.E,
                 bg="white",  # Background Color
                 fg="grey",  # Foreground Color --> Font Color
                 borderwidth=4,
                 relief="groove"
                 ).grid(row=0, column=0, columnspan=4, sticky=tk.E)

    def add_string(self, what: str):
        print(f"{what} gedrückt")  # TODO Cleanup
        if self.text_var.get() == '0':
            self.text_var.set(what)
        else:
            self.text_var.set(self.text_var.get() + what)

    def add_button(self, brow: int, bcol: int, bstr: str, myaction: str):
        pixel = tk.PhotoImage(width=1, height=1)
        print(myaction)  # TODO Cleanup
        act_button = tk.Button(self,
                               text=bstr,
                               image=pixel,  # TODO PixelImage ??
                               width=10,
                               height=10,
                               compound='c',
                               command=lambda: self.add_string(bstr))
        act_button.grid(row=brow, column=bcol, sticky=tk.W)
        self.update()


def main():
    # TODO: add '<-' 'C' 'sqrt' utf_8('U+221A')
    butt: list[str] = ['1', '2', '3', '+',
                       '4', '5', '6', '-',
                       '7', '8', '9', '*',
                       '.', '0', '=', '/']
    actions: list[str] = ['number', 'number', 'number', 'plus',
                          'number', 'number', 'number', 'minus',
                          'number', 'number', 'number', 'times',
                          'number', 'number', 'calculate', 'devide']

    myCalc = Rechner()
    for num, (text, action) in enumerate(zip(butt, actions)):
        # got 16 buttons make 4 each row, num // 4 is the row
        # num % 4 ist the col, text is label on button
        # action is what to do, add_button(row, col, str, myaction)
        myCalc.add_button((num // 4)+1, num % 4, text, action)

    # myCalc.add_button(1, 0, "1", 1)  #TODO cleanup
    # myCalc.add_button(1, 1, "2", 0)  #TODO cleanup
    # myCalc.add_button(1, 2, "3", 0)  #TODO cleanup
    # myCalc.add_button(1, 3, "4", 0)  #TODO cleanup
    # myCalc.add_button(2, 1, "+", 1)  #TODO cleanup
    # myCalc.text_var.set('2')
    myCalc.add_string('5')
    myCalc.mainloop()


if __name__ == '__main__':
    main()
