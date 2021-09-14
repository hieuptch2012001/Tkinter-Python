import tkinter as tk
from time import time


def message():
    print('Good morning')


on = 1
root = tk.Tk()

start = time()


def close_frame():
    global on, frame, lbx
    if on:
        frame.pack_forget()
        on = 0
    else:
        frame.pack_forget()
        frame1.pack_forget()
        create_frame()
        on = 1


def print_size():
    root.update()
    print("Screen width:", root.winfo_width())
    print("Screen height:", root.winfo_height())
    root.after(100, print_size)


def create_frame():
    """create frame to be hidden when we press k"""
    global lbx, lbx1, frame, frame1

    frame = tk.Frame(root)
    frame.pack(side="left")
    lbx = tk.Listbox(frame, bg="gold")
    lbx.pack()
    lbx.insert(0, 1)
    frame1 = tk.Frame(root)
    frame1.pack()
    lbx1 = tk.Listbox(frame1, bg="cyan")
    lbx1.pack(side="left")
    lbx1.insert(0, 2)


create_frame()

button1 = tk.Button(root, text="Demo Button", command=close_frame)
button2 = tk.Button(root, text="print Button", command=print_size)
message()
# root.bind("&lt;k>", close_frame)
button1.pack(side="left")
button2.pack(side="right")
root.after(100, print_size)
root.mainloop()
