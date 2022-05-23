# GUI : Graphical User Interface

import os
from pathlib import Path
os.chdir(Path(__file__).parent)
from tkinter import Tk, Scale, TOP, VERTICAL, LEFT, RIGHT, END, DISABLED, NORMAL, Entry, Label
from tkinter import IntVar, Radiobutton, Checkbutton, Canvas, Frame, Menu, Text, Button, PhotoImage, messagebox, ttk

# 1. Create windows instance
window = Tk()


def main_window():
    # Change title
    window.title("WBS Training")

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


def label_widget():

    # Define the label
    label = Label(window,
                  text="Hello WBS",
                  font=("Ink Free", 20, "bold"),

                  padx=10,  # Padding x
                  pady=10,  # Padding y

                  bg="red",  # Background Color
                  fg="blue"  # Foreground Color --> Font Color
                  )

    # Show the widget

    #  label.place(x= 0 , y= 90)
    label.pack()   # Top - Center of the container


def button_widget():

    def click_me():
        print("Hello Button from Tkinter 2")

    # define a button
    button = Button(window,
                    text="Click Me",
                    font=("Ink Free", 20, "bold"),

                    bg="yellow",
                    fg="blue",

                    padx=20,
                    pady=30,

                    command=click_me,
                    # state= ACTIVE, # DISABLED
                    )

    # show the button on the container
    button.pack()


def entry_widget():

    def show_value():
        # Get the Value from the EntryBox
        message = entry.get()
        print(message)

        # Disable the EntryBox
        entry.config(
            state=DISABLED
        )

    def delete_value():
        entry.config(
            state=NORMAL,
            show=""  # normal text format wieder
        )

        entry.delete(0, END)  # from Charachter 0 to the END: last charachter

    def insert_text():
        entry.insert(0, "Welcome Mohamed")   # 0 : first charachter

    entry = Entry(window,
                  font=("Arial", 20),
                  fg="red",
                  bg="yellow",
                  show="*"  # like a password
                  )

    button_show_value = Button(window, text="Show Value", command=show_value)
    button_delete = Button(window, text="Delete Value", command=delete_value)
    button_add_text = Button(window, text="Add Text", command=insert_text)

    # Show the widgets on the screen
    entry.pack(side=LEFT)
    button_show_value.pack(side=RIGHT)
    button_delete.pack(side=RIGHT)
    button_add_text.pack(side=RIGHT)


def checkbutton_widget():

    def display_value():
        if x.get() == 1:
            print("The user clicked True")
        elif x.get() == 0:
            print("The user clicked False")

    x = IntVar()  # StringVar() , BooleanVar()

    checkbutton = Checkbutton(window,
                              text="ich habe alles verstanden",
                              width=50,

                              fg="red",
                              bg="blue",
                              font=("Arial", 30),

                              variable=x,

                              onvalue=1 ,  # if the checkbutton True--> store 1
                              offvalue=0,  # if the checkbutton False--> store 0

                              command=display_value
                              )

    checkbutton.pack()


def radiobutton_widget():

    def user_wish():

        if x.get() == 0:
            print("The user has Pizza")
        elif x.get() == 1:
            print("The user has Auflauf")
        elif x.get() == 2:
            print("The user has Salat")

    foods = ["Pizza", "Auflauf", "Salat"]
    x = IntVar()  # starts with 0

    for idx in range(len(foods)):

        radio_button = Radiobutton(
            window,
            text=foods[idx],
            value=idx,  # 0 , 1, 2
            variable=x,
            command=user_wish
        )

        radio_button.pack()


def scale_widget():

    def show_value():
        print(f"The value of the scale is {scale.get()}")

    # Define the widget
    scale = Scale(window,
                  from_=0,
                  to=100,
                  length=200,
                  orient=VERTICAL ,  # HORIZONTAL
                  tickinterval=10,
                  resolution=0.5,  # the step
                  showvalue=1 ,  # show current value , 1 or 0
                  troughcolor="red",

                  )

    button = Button(window,
                    text="Show value",
                    command=show_value)

    # Define a value to the scale
    scale.set(70)

    # Show on screen
    scale.pack()
    button.pack()


def messagebox_widget():

    def show_message_box():
        # 1. Info
        #########
        # messagebox.showinfo(title = "Info 1", message="You are a good person")
        # messagebox.showwarning(title = "Warning 1", message="Storage space will be full soon!!")
        # messagebox.showerror(title = "Error 1", message="The file does not exist..!!")

        # 2. User Reaction
        ############################
        # if messagebox.askokcancel(title="Ask ok or cancel 1", message="Do you want to continue ?"):   # return Boolean
        #     print("The user has choosed : True")
        # else:
        #     print("The user has choosed : False")

        # if messagebox.askretrycancel(title="Try again?", message="Retry copying the files ?"):   # return Boolean
        #     print("The user has choosed : True")
        # else:
        #     print("The user has choosed : False")

        # if messagebox.askyesno(title="Yes or No?", message="have you payed your bill ?"):   # return Boolean
        #     print("The user has choosed : True")
        # else:
        #     print("The user has choosed : False")

        # result = messagebox.askyesnocancel(title="Yes or No or Cancel?", message="have you payed your bill ?")
        # #  return True, False, None
        # if result == True:
        #     print("The user has choosed : True")
        # elif result == False:
        #     print("The user has choosed : False")
        # elif result == None:
        #     print("The user has choosed : Cancel")

        result = messagebox.askquestion(title="Question 1", message="Are you tired?")  # Return a string yes, no
        print(result)

    button = Button(window,
                    text="Show Message Box",
                    command=show_message_box)

    button.pack()


def textarea_widget():

    def show_value():
        print(text.get(1.0 , END))   # 1.0 Start Charachter,   END: end charachter

    # Define the GUI-control
    text = Text(window,
                height=3,  # count of charachters
                width=50,  # count of charachters
                font=("Ink Free", 14),
                fg="red",
                bg="yellow",)

    button = Button(window, text="Show value", command=show_value)

    # Place the control on the screen
    text.pack()  # Top center
    button.pack()


def menu_widget():

    def new_file():
        messagebox.showinfo(title="Menu Widget", message="New file is clicked!")

    def open_file():
        messagebox.showinfo(title="Menu Widget", message="Open file is clicked!")

    def save_file():
        messagebox.showinfo(title="Menu Widget", message="Save file is clicked!")

    def cut():
        pass

    def copy():
        pass

    # Define the menu
    menubar = Menu(window)

    # Attach the menu to the window
    window.config(menu=menubar)

    # Create Menus "Categories"
    file_menu = Menu(menubar, tearoff=0)  # tearoff : to hide the splitter ---
    edit_menu = Menu(menubar, tearoff=0)  # tearoff : to hide the splitter ---

    # Create sub menus

    file_menu.add_command(label="New File", command=new_file)
    file_menu.add_command(label="Open File", command=open_file)
    file_menu.add_command(label="Save File", command=save_file)

    file_menu.add_separator()

    file_menu.add_command(label="Exit", command=quit)

    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)

    # Show the menu to the main menu bar
    menubar.add_cascade(label="File", menu=file_menu)
    menubar.add_cascade(label="Edit", menu=edit_menu)


def frame_widget():
    # Frame is container like a window

    frame = Frame(window)

    Button(frame, text="Up", font=("Arial", 20), width=9).pack(side=TOP)
    Button(frame, text="Left", font=("Arial", 20), width=9).pack(side=LEFT)
    Button(frame, text="Down", font=("Arial", 20), width=9).pack(side=LEFT)
    Button(frame, text="Right", font=("Arial", 20), width=9).pack(side=LEFT)

    # frame.pack()
    frame.place(x=100, y=200)


def tabs_widget():
    notebook = ttk.Notebook(window)

    # Create TABS
    tab1 = Frame(notebook)
    tab2 = Frame(notebook)

    # Create Widgets within the TAB
    Label(tab1, text="This is my label 1").pack()
    Label(tab1, text="This is my label 2").pack()
    Label(tab1, text="This is my label 3").pack()

    Button(tab2, text="This is my Button 1").pack()
    Button(tab2, text="This is my Button 2").pack()
    Button(tab2, text="This is my Button 3").pack()

    # Add the TABS to the Notebooks
    notebook.add(tab1, text="TAB 1")
    notebook.add(tab2, text="TAB 2")

    notebook.pack(expand=True, fill="both")


# def grid_structure():
#     title = Label(window, text="User Registration", font=("Arial", 30)).grid(row=0, column=0, columnspan=2)

#     lbl_first_name = Label(window, text="First name").grid(row=1, column=0)
#     entry_first_name = Entry(window).grid(row=1, column=1)

#     lbl_last_name = Label(window, text="Last name").grid(row=2, column=0)
#     entry_last_name = Entry(window).grid(row=2, column=1)

#     submit = Button(window, text="Submit").grid(row=3, column=1)


def canvas_widget():
    canvas = Canvas(window)

    canvas.create_line(0, 0, 300, 300, fill="red", width=5)
    canvas.create_line(0, 300, 150, 180, fill="blue", width=5)
    canvas.create_rectangle(5, 5, 80, 80, fill="yellow", width=5)
    canvas.create_polygon(100, 100, 200, 200, 0, 200, fill="purple", outline="black")
    canvas.create_arc(0, 0, 50, 50, fill="green", start=90, extent=180)  # start= the angle of the

    canvas.pack()


def keyboard_event():

    def show_key(event):
        print("The key is:", event.keysym)  # Keysym : Key Symbol

        key_catalog = {
            "a": "Alpha",
            "b": "Berta"
        }

        # if event.keysym == "a":
        #     label.config(text= "Alpha")
        # else:
        #     label.config(text= event.keysym)

        print(key_catalog.get(event.keysym , "Not found"))
        label.config(text=key_catalog.get(event.keysym , "Not found"))

    # Bind the keyboard to the window --> Catch the keyboard keys
    window.bind("<Key>", show_key)

    label = Label(window, font=("Arial", 50))
    label.pack()


def mouse_events():

    def catch_event(event):
        print("Mouse Position:", event.x, event.y)

    # window.bind("<Button-1>", catch_event) # left mouse click
    # window.bind("<Button-2>", catch_event) # Scroll wheel mouse
    # window.bind("<Button-3>", catch_event) # right mouse click

    # window.bind("<Enter>", catch_event) # when the mouse pointer enters the window
    # window.bind("<Leave>", catch_event) # when the mouse pointer leave the window
    # window.bind("<Motion>", catch_event) # when the mouse pointer moves on the window

    window.bind("<ButtonRelease>", catch_event)  # when the mouse click goes up


def drag_drop_effect():

    def drag_start(event):
        widget = event.widget

        widget.start_x = event.x
        widget.start_y = event.y

    def drag_motion(event):
        widget = event.widget
        # winfo_x: returns the x postion of the upper left corner to the parent widget
        x_new = widget.winfo_x() - widget.start_x + event.x
        # winfo_y: returns the y postion of the upper left corner to the parent widget
        y_new = widget.winfo_y() - widget.start_y + event.y

        widget.place(x=x_new, y=y_new)

    label = Label(window, bg="red", width=10, height=10)
    label2 = Label(window, bg="yellow", width=10, height=10)

    label.place(x=0, y=0)
    label2.place(x=100, y=0)

    label.bind("<Button-1>", drag_start)
    label.bind("<B1-Motion>", drag_motion)

    label2.bind("<Button-1>", drag_start)
    label2.bind("<B1-Motion>", drag_motion)


def main():
    # Adjust the main_window
    main_window()

    # 1. Label Widget
    # label_widget()

    # 2. Button Widget
    button_widget()

    # 3. Entry Widget
    # entry_widget()

    # 4. CheckButton
    # checkbutton_widget()

    # 5. RadioButton
    # radiobutton_widget()

    # 6. Scale
    # scale_widget()

    # 7. MessageBoxes
    # messagebox_widget()

    ######################################################################

    # 8. Textarea Widget
    # textarea_widget()

    # 9. Menu Widget
    # menu_widget()

    # 10. Frame
    # frame_widget()

    # 11. TABS Widget
    # tabs_widget()

    # 12. Grid_Structure
    # grid_structure()

    # 13. Canvas
    # canvas_widget()

    # 14. KeyBoard Event
    # keyboard_event()

    # 15. Mouse Events
    # mouse_events()

    # 16. DragDrop Effect
    # drag_drop_effect()

    # Show the main Window
    window.mainloop()


main()
