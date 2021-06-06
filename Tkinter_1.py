# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-4
# todo : Label, Geometry, Maxsize & Minsize

from tkinter import *
root = Tk()

# Width x Height
root.geometry("644x434")
# width, height
root.minsize(300,100)
# width, height
root.maxsize(1200, 988)
label1 = Label(text="This is My First Program in tkinter course 1")
label1.pack()

root.mainloop()
