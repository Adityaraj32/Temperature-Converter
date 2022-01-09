from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Temperater Converter")
root.wm_iconbitmap("Temperature.ico")
root.geometry("499x500")

# This function will convert celcius to fahrenheit 
def Convert():
    if FahOrCel.get()==1:
        Celcius = Temperature.get()
        Fahrenheit = (float(Celcius)*9/5+ 32)
        tmsg.showinfo("Conversion Succsfull!",f"{Celcius} Celcius is {Fahrenheit} Fahrenheit")
# This function will convert fahrenheit to celcius 
    elif FahOrCel2.get()==1:
        Fahrenheit = Temperature.get()
        Celsius = (float(Fahrenheit) - 32) / 1.8
        tmsg.showinfo("Conversion Succsfull!",f"{Fahrenheit} Fahrenheit is {Celsius} Celsius")


# Main Heading of the program
# font="lucida 20 bold"
frame = Frame(root, bg="yellow", borderwidth=10, relief=SUNKEN).grid(row=1,column=3)
# Txt = Label(frame,text="Temperature Converter",fg="green", font="comicsansms 10 bold",padx=15).grid(row=0,column=3)

Txt1 = Label(text="Temperature",font="Cascadia 20").grid(row=4,column=1)
Temperature = IntVar()
TemEnt = Entry(root, textvariable=Temperature,width=10,font="Cascadia 15 bold").grid(row=4,column=2,padx=5)

FahOrCel = IntVar()
Temp = Checkbutton(text="Celcius", variable = FahOrCel).grid(row=4, column=3)
FahOrCel2 = IntVar()
Temp2 = Checkbutton(text="Fahrenheit", variable = FahOrCel2).grid(row=4, column=4)

convert = Button(root,text="Convert It!",font="Cascadia 15 bold",command=Convert).grid(row=15,column=2)

root.mainloop()