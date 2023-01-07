import tkinter as tk


class Window:
    """
    Window Class
        - Handles Tkinter window, determines transparency and initalisation
    """

    def __init__(self):
        self.root = tk.Tk("The Fang")
        self.root.title("The Fang")
        self.root.geometry("1000x500")
        self.root.call('tk', 'scaling', 10.0)

    def mainloop(self):
        self.root.resizable(False, False)
        self.root.configure(bg='black')
        self.root.attributes("-alpha", 0.9)
        self.root.mainloop()

    def get_root(self):
        return self.root
