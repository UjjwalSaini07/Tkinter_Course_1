# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-19
# todo : Sliders In Tkinter Using Scale()

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Slider tutorial")

# get(): This method returns the current value of the scale.
# set(value): It sets the scale's value. For example, if we give set(30) the initial scale value will show 30 (the scale will starts from 30).

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} dollars to your bank account")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider2.set(34)
myslider2.pack()
Button(root, text="Get dollars!", pady=10, command=getdollar).pack()

root.mainloop()