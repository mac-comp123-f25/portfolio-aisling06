import tkinter as tk
from tkinter import ttk    # Creates widgets with OS look-and-feel

class FrameExample:
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Frame example")
        f1 = tk.Frame(self.rootWin, bg = "lightblue", bd=5,
                      relief=tk.SUNKEN, padx = 10, pady = 10)
        f1.grid(row = 1, column = 1)
        f2 = tk.Frame(self.rootWin, bg = "pink", bd=5,
                      relief=tk.SUNKEN, padx = 10, pady = 10)
        f2.grid(row = 1, column = 2)


        # Builds lists containing Button objects
        self.frame1Buttons = []
        self.frame2Buttons = []
        for i in range(3):
            bName = "F1 Button" + str(i)
            button = ttk.Button(f1, text = bName) # font="Arial 14")
            button.grid(row = i, column = 1, padx=10, pady=10)
            self.frame1Buttons.append(button)
        for i in range(3):
            bName = "F2 Button" + str(i)
            button = ttk.Button(f2, text = bName) # font="Arial 14")
            button.grid(row = 1, column = i, padx=10, pady=10)
            self.frame2Buttons.append(button)

    def run(self):
        self.rootWin.mainloop()


# Main program:
frameGui = FrameExample()
frameGui.run()
