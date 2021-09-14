from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text")

text = Text(root, height=8)
text.pack()

text.insert('3.0', 'This is a text')

root.mainloop()
