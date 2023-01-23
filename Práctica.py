import tkinter as tk
from random import randint
from tkinter import messagebox
vent=tk.Tk()
vent.title("To My Valentine")
vent.geometry('300x300')
def move_btn(event):
    event.widget.place(x=randint(0,250), y=randint(0,250))

def pressed():
    messagebox.showinfo("title", "I knew you'd say yes <3")

title=tk.Label(vent, text='Would you be my GF?')
title.pack(padx=20, pady=20)

button1=tk.Button(vent, text='NO', height='1', width='8')
button1.place(x=180, y=170)
button1.bind("<Enter>", move_btn)
button2=tk.Button(vent, text='YES', height='1', width='8', command=pressed)
button2.place(x=50, y=170)


vent.mainloop()
