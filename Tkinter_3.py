# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-6
# todo : Attributes Of Label & Pack

from tkinter import *
root = Tk()
root.geometry("744x373")
root.title("My GUI")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''
Python is an interpreted high-level \ngeneral-purpose programming language.\nPython's design philosophy emphasizes code readability \nwith its notable use of significant indentation.\nIts language constructs as well as its object-oriented \napproach aim to help programmers write clear,\nlogical code for small and large-scale projects.''', bg ="black", fg="white", padx=13, pady=94, font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx ; pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=TOP, fill=BOTH, padx=34, pady=34)

root.mainloop()
