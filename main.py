from main.MainApplication import MainApplication
import tkinter as tk
from window.Window import Window

if __name__ == "__main__":
    window = Window()
    MainApplication(window.get_root(), background='black') \
        .pack(side="top", fill="both", expand=True)
    window.mainloop()