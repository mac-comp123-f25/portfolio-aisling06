# ------------------ First section: import statements -----------------
import tkinter as tk


# ------------------ Second section: class and methods ----------------

class BasicGui:
    def entryResponse(self, event):
        if event.keysym == "Return":  # examples of how to check what key
            print("Return pressed")  # was pressed
        elif event.keysym == "Tab":
            print("Tab pressed")
        txt = self.testEntry.get()  # get Entry widget’s text
        revTxt = txt[::-1]  # make a copy in reverse order
        self.testEntry.delete(0, tk.END)  # remove old Entry text
        self.testEntry.insert(0, revTxt)  # place reversed text in Entry

    def __init__(self):
        self.rootWin = tk.Tk()
        self.newLabel = tk.Label(self.rootWin, text="", font="Arial 14")
        self.newLabel.grid(row=0, column=0, pady=10)
        self.testEntry = tk.Entry(self.rootWin, bg='pink', bd=5, font="Times 12",
                             justify=tk.CENTER, relief=tk.GROOVE, width=40)
        self.testEntry.grid(row=2, column=2)
        testButton = tk.Button(self.rootWin)
        testButton["text"] = "Copy"
        testButton["font"] = "Arial 12"
        testButton["bg"] = "#997711"
        testButton["fg"] = "blue"
        testButton.grid(row=1, column=0)
        testButton["command"] = self.testButtonResponse

    def run(self):
        self.rootWin.mainloop()

    def testButtonResponse(self):
        txt = self.testEntry.get()  # get text user typed in Entry box
        self.newLabel["text"] = txt  # display that text in a label
        print("clicked")


# ------------------ Third section: main program ----------------------

myGui = BasicGui()
myGui.run()
