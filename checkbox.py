import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Checkbox')

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Ressult', message=agreement.get())


ttk.Checkbutton(root,
                text='i agree',
                command=agreement_changed,
                variable=agreement,
                onvalue='agree',
                offvalue='disagree').pack()

root.mainloop()
