# https://www.codewithharry.com/videos/python-gui-tkinter-hindi-15
# todo : Creating newspaper GUI

from tkinter import *
from PIL import  ImageTk, Image
import tkinter.ttk as ttk
import webbrowser

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

def web_1():
    webbrowser.open("https://www.hindustantimes.com/india-news/dear-bjp-why-do-you-hate-delhi-aap-asks-as-centre-blocks-ration-scheme-101622902022688.html")
def web_2():
    webbrowser.open("https://www.hindustantimes.com/india-news/gst-revenue-crosses-rs-100-000-crore-mark-for-8th-straight-month-collection-at-rs-102-709-crore-101622893679243.html")

root = Tk()
root.title("THE TIMES OF INDIA")
root.geometry("900x1000")

texts = []
photos = []

for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    image = image.resize((225, 265), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))


f0 = Frame(root, width=800, height=70)
Label(f0, text="THE TIMES OF INDIA", font="lucida 33 bold").pack()
Label(f0, text="5 JUNE 2021", font="lucida 18 bold").pack()
f0.pack()

f1 = Frame(root, width=900, height=120, pady=14)
Label(f1, text=texts[0], padx=18, pady=22, font="lucida 10").pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
Button(f1,text="Open on Webpage",font="lucida 11 bold",command=web_1).pack()
f1.pack(anchor="w")

f2 = Frame(root, width=900, height=120, pady=14, padx=22)
Label(f2, text=texts[1], padx=18, pady=22).pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
Button(f2,text="Open on Webpage",font="lucida 11 bold",command=web_2).pack()
f2.pack(anchor="w")

f3 = Frame(root, width=900, height=200, pady=34)
Label(f3, text=texts[2], padx=18, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()

