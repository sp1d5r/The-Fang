from tkinter import *

gui = Tk(className='Python Examples - Window Color')
# set window size
gui.geometry("400x200")

#set window color
gui.configure(bg='black')
gui.attributes("-alpha", 0.8)
gui.mainloop()