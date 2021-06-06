# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-18
# todo : Message Box In Tkinter Python

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("733x566")
root.title("Pycharm")

def myfunc():
    print("FUNCTION RUNNING PROPERLY")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "Ujjwal will help you with this gui")

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)

def function_1():
    ans = tmsg.askretrycancel("Trip", "You Interested to go to trip")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")

    else:
        print("Bahut badiya bhai cancel kar diya warna pitte")
def function_2():
    ans = tmsg.showerror("Error","Your System Crashed")
def function_3():
    ans = tmsg.askokcancel("Please Give your Opinion","You Re-run the program")
def function_4():
    ans = tmsg.askyesno("Please Give your Opinion","We become Friends")
def function_5():
    ans = tmsg.askretrycancel("Program Smashed","Are You re-use The program")
def function_6():
    ans = tmsg.askyesnocancel("Checking","Are you ssave the program")
def function_7():
    ans = tmsg.showwarning("Warning","Program Deleted")

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="yes_no_cancel", command=function_6)
m1.add_command(label="warning", command=function_7)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Error", command=function_2)
m2.add_command(label="Okay_cancel", command=function_3)
m2.add_separator()
m2.add_command(label="yes_no", command=function_4)
m2.add_command(label="retry_cancel", command=function_5)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label = "Help", command=help)
m3.add_command(label = "Rate us", command=rate)
m3.add_command(label = "ask_retry", command=function_1)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)

root.mainloop()

# from tkinter import *
# from tkinter import messagebox
# root = Tk()
# root.geometry("300x200")
# w = Label(root, text ='GeeksForGeeks', font = "50")
# w.pack()
# messagebox.showinfo("showinfo", "Information")
# messagebox.showwarning("showwarning", "Warning")
# messagebox.showerror("showerror", "Error")
# messagebox.askquestion("askquestion", "Are you sure?")
# messagebox.askokcancel("askokcancel", "Want to continue?")
# messagebox.askyesno("askyesno", "Find the value?")
# messagebox.askretrycancel("askretrycancel", "Try again?")
# root.mainloop()
#
