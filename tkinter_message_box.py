import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning

# creat the root window
root = tk.Tk()
root.title("Tkinter messagebox")
root.resizable(False, False)
root.geometry("500x500")

options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

ttk.Button(
    root,
    text="Show an error message",
    command=lambda: showerror(
        title='Error',
        message='This is an error message'
    )
).pack(options)

ttk.Button(
    root,
    text='Show an information message',
    command=lambda: showinfo(
        title='Information',
        message='This is an information message.')
).pack(options)

ttk.Button(
    root,
    text='Show an warning message',
    command=lambda: showwarning(
        title='Warning',
        message='This is a warning message.')
).pack(options)

root.mainloop()
