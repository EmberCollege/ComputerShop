# Main tkinter page for Computer Shop project - Rhys Matthews

import tkinter as tk

class Main():

    def __init__(self, master) -> None:
        self.master = master

        master.title = "Computers UK Store"

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(False,False)
    main = Main(root)
    root.mainloop()

    