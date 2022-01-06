import tkinter
from tkinter import *
from tkinter import font
import tkinter.messagebox as tmsg
root = Tk()
root.title("Temperater Converter")
root.wm_iconbitmap("Temperature.ico")
tkinter.font.NORMAL
tkinter.font.BOLD
tkinter.font.ITALIC
tkinter.font.ROMAN
root.geometry("499x500")
root.minsize("499","500")
root.maxsize("499","500")

def CelToFah():
    Celcius = None
    Fahrenheit = (Celcius * 9/5) + 32

def FahToCel():
    Fahrenheit = None
    Celsius = (Fahrenheit - 32) / 1.8

# Frame1 = Frame(root,borderwidth = 10,relief = SUNKEN,pady = 50)
# Frame1.grid()

Txt = Label(text="Temperature Converter",fg="green",font="lucida 25 bold italic")
Txt.pack(anchor=CENTER)
# Txt.grid(row= 0,column= 1)
Txt1 = Label(text="Temperature",font="lucida 20 bold")
Txt1.pack(side=LEFT,anchor="ne")
# Txt1.grid(row= 3,column= 1)

Temperature = StringVar()
TemEnt = Entry(root, textvariable=Temperature,width=30)
TemEnt.pack(side=LEFT,anchor="ne",ipady=5,pady=5)
# TemEnt.grid(row= 3,column= 2,ipady=15)

root.mainloop()