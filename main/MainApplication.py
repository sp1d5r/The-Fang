import tkinter as tk
from title.Title import Title


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title = Title(self, width=1000, height=57)

        self.title.pack(side="top", pady=10)


