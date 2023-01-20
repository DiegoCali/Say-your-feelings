import tkinter as tk
from random import randint
from tkinter import messagebox
vent=tk.Tk()
vent.title("El conquista minas 3000")
vent.geometry('300x300')
def move_btn(evento):
    evento.widget.place(x=randint(0,250), y=randint(0,250))

def pressed():
    messagebox.showinfo("titulo", "Sabía que aceptarías :3")

titulo=tk.Label(vent, text='¿Quiéres ser mi novia?')
titulo.pack(padx=20, pady=20)

boton1=tk.Button(vent, text='NO', height='1', width='8')
boton1.place(x=180, y=170)
boton1.bind("<Enter>", move_btn)
boton2=tk.Button(vent, text='SI', height='1', width='8', command=pressed)
boton2.place(x=50, y=170)


vent.mainloop()
