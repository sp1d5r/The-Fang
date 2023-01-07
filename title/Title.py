import tkinter as tk
from PIL import Image, ImageTk

class Title(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        load = Image.open("./assets/Title.png")
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render, background='black')
        img.image = render
        img.pack(side="top")

