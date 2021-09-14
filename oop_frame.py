from tkinter import ttk
import tkinter as tk


class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.setupWidgets()

    def setupWidgets(self):
        button1 = ttk.Button(self, text="Button 1")
        button1.grid(row=0, column=0, sticky=tk.NSEW)

        button2 = ttk.Button(self, text="Button 2")
        button2.grid(row=0, column=1, sticky=tk.NSEW)

        button3 = ttk.Button(self, text="Button 3")
        button3.grid(row=1, column=0, sticky=tk.NSEW)


class treeviewFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.widgetsSetup()

    def widgetsSetup(self):
        button4 = ttk.Button(self, text="Button 4")
        button4.grid(row=0, column=0, sticky=tk.NSEW)

        button5 = ttk.Button(self, text="Button 5")
        button5.grid(row=0, column=1, sticky=tk.NSEW)


class mainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("500x500")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.crate_frame()

    def crate_frame(self):
        input_frameMain = MainFrame(self)
        input_frameMain.grid(row=0, column=0, sticky=tk.NSEW)

        input_frameTreeView = treeviewFrame(self)
        input_frameTreeView.grid(row=0, column=1, sticky=tk.NSEW)


def main():
    app = mainApp()

    frameMain = MainFrame(app)
    frameTreeView = treeviewFrame(app)

    app.mainloop()


if __name__ == '__main__':
    main()
