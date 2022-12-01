import tkinter as tk


class Element(tk.Tk):
    def __init__(self, _label, _action):
        self.label = _label
        self.action = _action


class Taste(Element):
    def __init__(self, _label, _action):
        super().__init__(_label, _action)



