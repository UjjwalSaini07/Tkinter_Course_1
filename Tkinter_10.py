# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-14
# todo : Handling Events In Tkinter GUI

from tkinter import *

def call(event):
    print(f"You clicked on the button at {event.x}, {event.y}")
root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")
widget = Button(root, text='Click me please')
widget.pack()
widget.bind('<Button>', call)
widget.bind('<Double-Button>', quit)

# todo : For More Information Visit-https://www.python-course.eu/tkinter_events_binds.php

root.mainloop()
