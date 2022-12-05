import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()

# for num, (text, action) in enumerate(zip(txt, code)):
#     # got 16 buttons make 4 each row, num // 4 is the row
#     # num % 4 ist the col, text is label on button
#     # code is what to do, add_button(row, col, str, code)
#     # print(f"Row {(num // 4)+1} Col {num % 4} ")
#     my_calc.add_button((num // 4) + 1, num % 4, text, action)
