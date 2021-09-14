from tkinter import *
from tkinter import ttk

    
def create_input_frame(parent):
    frame_input = ttk.Frame(parent)
    frame_input.columnconfigure(0, weight = 1)
    frame_input.columnconfigure(1, weight = 3)

    label_find = ttk.Label(frame_input, text = "Find :")
    label_find.grid(column=0, row = 0, sticky = W)
    
    label_replace = ttk.Label(frame_input, text = "Replace with :")
    label_replace.grid(column=0, row = 1, sticky = W)

    entry_find = ttk.Entry(frame_input)
    entry_find.grid(column=1, row = 0)

    entry_replace = ttk.Entry(frame_input)
    entry_replace.grid(column = 1, row = 1)

    match_case = StringVar()
    checkbutton_match_case = ttk.Checkbutton(frame_input, text = "Match case", variable=match_case, command=lambda: print(match_case.get()))
    checkbutton_match_case.grid(column=0, row = 2)

    return frame_input

def create_button_frame(parent):
    frame_button = ttk.Frame(parent)

    frame_button.columnconfigure(0, weight = 1)

    find_next_button = ttk.Button(frame_button, text = "Find Next")
    find_next_button.grid(column = 0, row = 0)
    replace_button = ttk.Button(frame_button, text = "Replace")
    replace_button.grid(column = 0, row = 1)
    replace_all_button = ttk.Button(frame_button, text = "Hide")
    replace_all_button.grid(column = 0, row = 2)
    replace_button = ttk.Button(frame_button, text = "Cancel", command = parent.destroy)
    replace_button.grid(column = 0, row = 4)

    return frame_button
    
def main_window():
    root = Tk()
    root.geometry("300x150")
    root.title("FrameTest")

    root.columnconfigure(0, weight = 4)
    root.columnconfigure(1, weight = 1)

    input_frame = create_input_frame(root)
    input_frame.grid(column = 0, row = 0)

    button_frame = create_button_frame(root)
    button_frame.grid(column= 1, row = 0)

    root.mainloop()

if __name__ == "__main__":
    main_window()