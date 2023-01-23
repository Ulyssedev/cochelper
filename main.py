import pygame
import os
from tkinter import *
app = Tk()
app.geometry("800x800")
app.title("CoC Helper @daniel_ptgl")
app.iconbitmap("pngcoc.ico")



#Background moment
bg_label = Label(app)
bg_image = PhotoImage(file="pngs/banger.png")
bg_label.configure(image=bg_image)
bg_label.image = bg_image
bg_label.pack()











app.mainloop()