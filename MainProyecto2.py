#Hoja de Trabajo 10
#Juan Diego Solorzano 18151
#Andrea Paniagua

from py2neo import *
from neo4j import *
from numpy import *
from tkinter import *
import tkinter.messagebox
from BaseDeDatos import *

window = Tk()
window.title("Sistema de Recomendacion")
window.configure(background="white")
window.geometry("900x800")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
dinero = "f"
actividad = ""
compan = ""
def selection():
    if (var1.get()==0 or var2.get()==0 or var3.get()==0):
        print("err")
        tkinter.messagebox.showinfo("Error", "Debe seleccionar una opcion para cada pregunta")
    else:
        valor = var1.get()
        if valor==1:
            dinero = "bajo"
            lo = "s"
            print("dsssd")
            print(dinero)
            h()
        elif valor==2:
            dinero = "medio"
        elif valor==3:
            dinero = "alto"
        

        valor2 = var2.get()
        if valor2==1:
            compan = "solo"
            print("dsssd")
        elif valor2==2:
            compan = "familia"
        elif valor2==3:
            compan = "pareja"
        elif valor2==4:
            compan = "amigos"

        valor3 = var3.get()
        if valor3==1:
            actividad = "aventura"
        elif valor3==2:
            actividad = "comida"
        elif valor3==3:
            actividad = "nocturno"
        elif valor3==4:
            actividad = "relajante"
            print("dsssd")
        
    res = recomendacion(dinero, compan, actividad)
    print(res)
def h():
    print(var1.get())
holaa()
scroll = Scrollbar(window)
#scroll.pack(side=RIGHT, fill=Y)
#scroll.grid(rowspan=4, column=5, pady=4, sticky = N+S)

Label(window, text="ACTIVIDADES Y LUGARES A VISITAR EN", bg="white", font="times 30 italic bold").grid(row=0, columnspan=6)
Label(window, text="GUATEMALA", bg="white", font="times 30 italic bold").grid(row=1, columnspan=6)


fotoGuate = PhotoImage(file="Guatemala.png")
foto= Label(window, image=fotoGuate, bg="white").grid(row=2, columnspan=6)


Label(window, text="Por favor ingrese los siguientes datos para realizar una recomendacion:", bg="white", font="times 20 bold").grid(row=3, column=0, columnspan=6)

Label(window, text="Presupuesto (Quetzales)", bg="white", font="times 16 bold").grid(row=4, column=1, sticky=E)
Label(window, text="Grupo a realizar actividad", bg="white", font="times 16 bold").grid(row=5, column=1, sticky=E)
Label(window, text="Tipo de actividad", bg="white", font="times 16 bold").grid(row=6, column=1, sticky=E)


Radiobutton(window, text="<200", bg="gray", fg="black",font="times 16 bold", value=1, variable = var1).grid(row=4,column=2,sticky=W)
Radiobutton(window, text="200-500", bg="gray", fg="black",font="times 16 bold", value=2, variable = var1).grid(row=4,column=3,sticky=W)
Radiobutton(window, text=">500", bg="gray", fg="black",font="times 16 bold", value=3, variable = var1).grid(row=4,column=4,sticky=W)

Radiobutton(window, text="Solo", bg="gray", fg="black",font="times 16 bold", value=1, variable = var2).grid(row=5,column=2,sticky=W)
Radiobutton(window, text="Familia", bg="gray", fg="black",font="times 16 bold", value=2, variable = var2).grid(row=5,column=3,sticky=W)
Radiobutton(window, text="Pareja", bg="gray", fg="black",font="times 16 bold", value=3, variable = var2).grid(row=5,column=4,sticky=W)
Radiobutton(window, text="Amigos", bg="gray", fg="black",font="times 16 bold", value=4, variable = var2).grid(row=5,column=5,sticky=W)

Radiobutton(window, text="Aventura", bg="gray", fg="black",font="times 16 bold", value=1, variable = var3).grid(row=6,column=2,sticky=W)
Radiobutton(window, text="Comida", bg="gray", fg="black",font="times 16 bold", value=2, variable = var3).grid(row=6,column=3,sticky=W)
Radiobutton(window, text="Nocturno", bg="gray", fg="black",font="times 16 bold", value=3, variable = var3).grid(row=6,column=4,sticky=W)
Radiobutton(window, text="Relajante", bg="gray", fg="black",font="times 16 bold", value=4, variable = var3).grid(row=6,column=5,sticky=W)


#Entry(window, bg="gray", fg = "white", font="times 16 bold italic").grid(row=4,column=2, sticky=W)
#Entry(window, bg="gray", fg = "white", font="times 16 bold italic").grid(row=5,column=2, sticky=W)
#Entry(window, bg="gray", fg = "white", font="times 16 bold italic").grid(row=6,column=2, sticky=W)

Button(window, text="INGRESAR", bg="black", fg="white", font="times 16 bold", command=selection).grid(row=12,columnspan=6)

window.mainloop()
