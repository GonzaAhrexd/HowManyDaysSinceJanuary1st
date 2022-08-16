

from tkinter import *
import tkinter as tk
interfaz=Tk()
interfaz.title("How many days")  #Título
interfaz.resizable(0,0)#Resizable
interfaz.geometry("650x350")#Resolución
interfaz.config(bg="#65f760")#Background



#Funciones


def sumar():
    day=int(caja1.get())  #Day
    segundo=int(caja2.get())  #Month

    if(segundo==1): #January
        mes2=0
    if(segundo==2): #February
        mes2=31
    if(segundo==3): #March
        mes2=59
    if(segundo==4): #April
        mes2=90
    if(segundo==5): #May
        mes2=120
    if(segundo==6): #June
        mes2=151
    if(segundo==7): #July
        mes2=181
    if(segundo==8): #August
        mes2=212
    if(segundo==9): #September
        mes2=243
    if(segundo==10): #October
        mes2=273
    if(segundo==11): #November
        mes2=304
    if(segundo==12): #December
        mes2=334

    if(bis.get()==1 and  segundo>=3):
        mes2=mes2+1


    sumar=(mes2+day)
   


    return resultado.set(sumar)

resultado=StringVar()
bis=tk.IntVar()

#Text
myLabel  = Label(interfaz, text= "How many days has passed since January 1st?", bg="#65f760",fg="blue",font=("Comic Sans MS", 20)).place(x=40, y=0)


#We require the day
textoLabel=Label(interfaz, text= "Type the day: ", bg="#65f760",fg="red").place(x=180,y=50)
caja1=Entry(interfaz)
caja1.place(x=260,y=50)

#We require the month
textoLabel=Label(interfaz, text= "Type the month*: ", bg="#65f760",fg="red").place(x=163,y=80)
textoLabel=Label(interfaz, text= "* Month must be in numbers (January=1, February=2...) ", bg="#65f760",fg="red").place(x=0,y=300)
caja2= Entry(interfaz)
caja2.place(x=260,y=80)


#Button
botonEnvio = Button(interfaz, text="Send",  command=sumar).place(x=300,y=200)
bisiesto = tk.Checkbutton(interfaz,text="Leap year",variable=bis, onvalue=1, offvalue=0).place(x=260,y=105)

#Final number
myLabel3  = Label(interfaz, text= "The current day is the number: ", bg="#65f760",fg="blue",font=("Comic Sans MS", 12)).place(x=205,y=145)


textoLabel=Label(interfaz, text= "Type the day: ", bg="#65f760",fg="red").place(x=180,y=50)
res= Entry(interfaz,textvariable=resultado).place(x=260,y=170)


interfaz.mainloop()