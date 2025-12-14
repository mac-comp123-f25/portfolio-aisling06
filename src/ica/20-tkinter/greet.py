import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        testButton = tk.Button(self.mainWin)
        testButton["text"] = "Quit"

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = BasicGui()
myGui.run()