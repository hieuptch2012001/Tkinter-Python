import tkinter as tk
from tkinter import Frame, ttk


def create(para):
    frame = ttk.Frame(para)

    frame.columnconfigure(0, weight=1)

    find_label = ttk.Label(frame, text='Find what:')
    find_label.grid(column=0, row=0, padx=20, pady=10, sticky=tk.W)
    find_entry = ttk.Entry(frame, width=30)
    find_entry.grid(column=1, row=0, sticky=tk.W)

    replace_label = ttk.Label(frame, text="Replace with:")
    replace_label.grid(column=0, row=1, padx=20, pady=10, sticky=tk.W)
    replace_entry = ttk.Entry(frame, width=30)
    replace_entry.grid(column=1, row=1, sticky=tk.W)

    return frame


def button_w(para):
    frame = ttk.Frame(para)

    frame.columnconfigure(0, weight=1)

    find_next_button = ttk.Button(frame, text="Find Next")
    find_next_button.grid(column=0, row=0, padx=0, pady=3)

    replace_button = ttk.Button(frame, text="Replace")
    replace_button.grid(column=0, row=1, padx=0, pady=3)

    replace_all_button = ttk.Button(frame, text="Replace All")
    replace_all_button.grid(column=0, row=2, padx=0, pady=3)

    cancel_button = ttk.Button(frame, text="Cancel")
    cancel_button.grid(column=0, row=3, padx=0, pady=3)

    return frame


def main():
    root = tk.Tk()

    root.geometry('500x500')
    # root.resizable(0, 0)

    root.columnconfigure(1, weight=5)
    root.columnconfigure(1, weight=1)

    label_frame = create(root)
    label_frame.grid(column=0, row=0)

    button_frame = button_w(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == '__main__':
    main()
