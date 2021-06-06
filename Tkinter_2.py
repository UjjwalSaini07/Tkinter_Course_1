# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-5
# todo : Displaying Images Using Label

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x600")
# photo = PhotoImage(file="1.png")
# For Jpg Images
image = Image.open("Photo.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()

root.mainloop()
