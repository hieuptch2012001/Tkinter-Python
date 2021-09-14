import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.resolution(False,False)
root.title('sapa')

ttk.Label(root, text="Fir").pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack()