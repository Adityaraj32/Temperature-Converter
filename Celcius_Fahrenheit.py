from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Temperater Converter")
root.geometry("499x500")
root.minsize("499","500")
root.maxsize("499","500")

def CelToFah():
    Celcius = None
    Fahrenheit = (Celcius * 9/5) + 32

def FahToCel():
    Fahrenheit = None
    Celsius = (Fahrenheit - 32) / 1.8

f1 = Frame(root,borderwidth = 10,relief = SUNKEN,pady = 50)
f1.grid()

Txt = Label(text="Temperature Converter",fg="green",font="lucida 20 bold italic")
Txt.grid(row= 0,column= 3)
Txt1 = Label(text="Temperature",font="lucida 15 bold italic")
Txt1.grid(row= 3,column= 1)

Temperature = StringVar()
TemEnt = Entry(root, textvariable=Temperature)
TemEnt.grid(row= 3,column= 2)

root.mainloop()