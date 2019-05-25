#Hoja de Trabajo 10
#Juan Diego Solorzano 18151
#Andrea Paniagua

from py2neo import *
from neo4j import *
from numpy import *
from tkinter import *
import tkinter.messagebox
from funciones import *

#variables
window = Tk()
window.title("Sistema de Recomendacion")
window.configure(background="white")
window.geometry("1300x800")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
strvar1 = StringVar()
strvar2 = StringVar()
strvar3 = StringVar()
dinero = ""
actividad = ""
compan = ""

#Funcion que recomienda en base de lo que selecciono
def ResultsPage():
    if (var1.get()==0 or var2.get()==0 or var3.get()==0):
        
        tkinter.messagebox.showinfo("Error", "Debe seleccionar una opcion para cada pregunta")
    else:
        valor = var1.get()
        if valor==1:
            dinero = "bajo"
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
            actividad = "comida rapida"
        elif valor3==3:
            actividad = "nocturno"
        elif valor3==4:
            actividad = "relajante"
        elif valor3==5:
            actividad = "comida nacional"
        elif valor3==6:
            actividad = "comida gourmet"
        
            
    #Muestra en pantalla los resultados segun el return de la funcion recomendacion   
    res = recomendacion(dinero, compan, actividad)
    x = 1
    t = "SEGUN TIPO DE ACTIVIDAD: \n"+ res[0]+"\n"
    p = "SEGUN PRESUPUESTO: \n"+ res[1]+ "\n"
    g = "SEGUN TAMANIO DE GRUPO: \n"+ res[2]+"\n"
    r = "RECOMENDACION FINAL (SATISFACE LAS TRES CONDICIONES): \n" + res[3]+ "\n"
    if len(res) >= 5:
        r = r + res[4] + res[5] +"\n"
        if len(res) >= 7:
            r = r + res[4] + res[5] +"\n"
            if len(res) == 9:
                r = r + res[8] + res[9] +"\n"
    
    top = Toplevel()
    top.title("Recomendaciones")
    top.geometry("1250x1100")
    fotoGuate2 = PhotoImage(file="gt.png")
    foto= Label(top, image=fotoGuate2, height = "300", bg="white").grid(row=0, column=6, columnspan=6)
    Label(top, text= t, bg="white", fg = "black", font="times 12 bold").grid(row=6, column=0, columnspan=2)
    Label(top, text= p, bg="white", fg = "black", font="times 12 bold").grid(row=6, column=10, columnspan=2)
    Label(top, text= g, bg="white", fg = "black", font="times 12 bold").grid(row=6, column=16, columnspan=2)
    Label(top, text= r, bg="white", fg = "black", font="times 12 bold").grid(row=7, column=10, columnspan=2)

    Button(top, text="EVALUAR RECOMENDACION", bg="black", fg="white", font="times 16 bold", command=EvaluatePage).grid(row=10,column=11, sticky=W)

def EvaluatePage():

    top2 = Toplevel()
    top2.title("Retroalimentacion")
    top2.geometry("500x450")
    Label(top2, text="RETROALIMENTACION", bg="white", font="times 30 italic bold").grid(row=0, columnspan=6)

    Label(top2, text="Nombre", bg="white", font="times 16 bold").grid(row=4, column=1, sticky=E)
    Label(top2, text="Edad", bg="white", font="times 16 bold").grid(row=5, column=1, sticky=E)
    Label(top2, text="Lugar a evaluar", bg="white", font="times 16 bold").grid(row=6, column=1, sticky=E)
    Label(top2, text="Le sirvio la recomendacion?", bg="white", font="times 16 bold").grid(row=7, column=1, sticky=E)

    entry1 = Entry(top2, bg="gray", fg = "white", font="times 16 bold italic", textvariable=strvar1).grid(row=4,column=2, sticky=W)
    entry2 = Entry(top2, bg="gray", fg = "white", font="times 16 bold italic", textvariable=strvar2).grid(row=5,column=2, sticky=W)
    entry3 = Entry(top2, bg="gray", fg = "white", font="times 16 bold italic", textvariable=strvar3).grid(row=6,column=2, sticky=W)
    Radiobutton(top2, text="Si", bg="gray", fg="black",font="times 16 bold", value=1, variable = var4).grid(row=7,column=2,sticky=W)
    Radiobutton(top2, text="No", bg="gray", fg="black",font="times 16 bold", value=2, variable = var4).grid(row=7,column=3,sticky=W)

    Button(top2, text="ENVIAR", bg="black", fg="white", font="times 16 bold", command=evaluate).grid(row=10,column=2, sticky=W)

def evaluate():
    nombreUsuario = strvar1.get()
    edadUsuario = strvar2.get()
    crearUsuario(nombreUsuario, edadUsuario)

    lugarEvaluado = strvar3.get()
    calif = ""
    valor4 = var4.get()
    if valor4 == 1:
        calif = "si"
    elif valor4 == 2:
        calif = "no"
    crearRating(nombreUsuario, lugarEvaluado, calif)

def StartPage():
    
    #Se crea interfaz
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
    Radiobutton(window, text="Comida Rapida", bg="gray", fg="black",font="times 16 bold", value=2, variable = var3).grid(row=6,column=3,sticky=W)
    Radiobutton(window, text="Nocturno", bg="gray", fg="black",font="times 16 bold", value=3, variable = var3).grid(row=6,column=4,sticky=W)
    Radiobutton(window, text="Relajante", bg="gray", fg="black",font="times 16 bold", value=4, variable = var3).grid(row=6,column=5,sticky=W)
    Radiobutton(window, text="Comida Nacional", bg="gray", fg="black",font="times 16 bold", value=5, variable = var3).grid(row=6,column=6,sticky=W)
    Radiobutton(window, text="Comida Gourmet", bg="gray", fg="black",font="times 16 bold", value=6, variable = var3).grid(row=6,column=7,sticky=W)


    

    #Cuando presiona el boton
    Button(window, text="INGRESAR", bg="black", fg="white", font="times 16 bold", command=ResultsPage).grid(row=10,columnspan=6)




    window.mainloop()
StartPage()

