#Hoja de Trabajo 10
#Juan Diego Solorzano 18151
#Andrea Paniagua 18

from py2neo import *
from neo4j import *
from numpy import *
from tkinter import *

db = Graph(password = "prueba123")


def crearUsuario(nombre, edad):
    db.run("CREATE (u:Usuario {name:'"+nombre+"', age:'"+edad+"'})")

def crearRating(nombre, lugar, leGusto):
    if leGusto == "si":
        db.run("MATCH (u:Usuario), (p:Place) WHERE u.nombre = '"+nombre+"' AND p.nombre = '"+lugar+"' CREATE (u)-[:LIKES]-> (p)")
def verificar(resul):

    if len(resul) != 0:
        resultado = resul
        
    elif len(resul) == 0:
        resultado = "No se encontraron recomendaciones"

    
    return resultado

def recomendacion(dinero, compan, actividad):

    #Encuentra segun tipo de actividad
    act = []
    nombres = db.run("MATCH (p:Place)-[:ES]->(t:Tourism) WHERE t.type = '"+actividad+"' RETURN p.nombre").to_ndarray()

    nombre = str(nombres)
    nomb = nombre.replace('[',"")
    nomb = nomb.replace("']","*")
    nomb = nomb.replace("]","")
    nomb = nomb.replace("'","")
    nomb = nomb.replace("\n","")
    no = nomb.split("*")
    x = 1
    entero = ""
    for i in no:
        if x != 11:
            entero = entero + str(x)+". " + i + "\n"
            x = x + 1
    act.append(str(entero))

    #Encuentra segun presupuesto
    doc = db.run("MATCH (p:Place)-[:TIENE]->(b:Budget) WHERE b.type = '"+dinero+"' RETURN p.nombre").to_ndarray()

    docs = str(doc)
    docs= docs.replace('[',"")
    docs = docs.replace("']","*")
    docs = docs.replace(']',"")
    docs = docs.replace("'","")
    docs = docs.replace("\n","")
    docs = docs.split("*")
    x = 1
    entero = ""

    for i in docs:
        if x != 11:
            entero = entero + str(x)+". " + i + "\n"
            x = x + 1

    act.append(str(entero))


    recomend = []
    for i in docs:
        for a in no:
            if str(i) == str(a):
                recomend.append(str(i))



    #Encuentra segun tamanio del grupo
    comp = db.run("MATCH (p:Place)-[:IR]->(c:Companion) WHERE c.type = '"+compan+"' RETURN p.nombre").to_ndarray()

    com = str(comp)
    com= com.replace('[',"")
    com = com.replace("']","*")
    com = com.replace(']',"")
    com = com.replace("'","")
    com = com.replace("\n","")
    com = com.split("*")
    x = 1
    entero = ""
    for i in com:
        if x != 11:
            entero = entero + str(x)+". " + i + "\n"
            x = x + 1

    act.append(str(entero))


    #Recomendacion con las tres condiciones ingresadas
    recomendar = []
    for i in com:
        for a in recomend:
            if str(i) == str(a) and str(i) != "":
                recomendar.append(str(i))

    rec = str(recomendar)
    rec= rec.replace('[',"")
    rec = rec.replace(']',"")
    rec = rec.replace("'","")
    rec = rec.replace("\n","")
    rec = rec.split(",")

    x = 1
    entero = ""
    for i in rec:
        if x != 11:
            entero = entero + str(x)+". " + i.lstrip() + "\n"
            x = x + 1

    act.append(str(entero))

    nombre1 = ""
    nombre2 = ""
    nombre3 = ""
    if len(rec) >= 1:
        nombre1 = str(rec[0]).lstrip()
        if len(rec) >= 2:
            nombre2 = str(rec[1]).lstrip()
            if len(rec) >= 3:
                nombre3 = str(rec[2]).lstrip()
        
    dir1 = db.run("MATCH (p:Place) WHERE p.nombre = '"+nombre1+"' RETURN p.direccion").to_ndarray()
    n1 = str(dir1)
    n1= n1.replace('[',"")
    n1 = n1.replace(']',"")
    n1 = n1.replace("'","")
    entero = "Direccion de " + nombre1+": "+n1 + "\n"
    act.append(str(entero))

    tel1 = db.run("MATCH (p:Place) WHERE p.nombre = '"+nombre1+"' RETURN p.telefono").to_ndarray()
    n1 = str(tel1)
    n1= n1.replace('[',"")
    n1 = n1.replace(']',"")
    n1 = n1.replace("'","")
    entero = "Telefono de " + nombre1+": "+n1 + "\n"
    act.append(str(entero))

    if len(rec) >2:
        dir1 = db.run("MATCH (p:Place) WHERE p.nombre = '"+nombre2+"' RETURN p.direccion").to_ndarray()
        n1 = str(dir1)
        n1= n1.replace('[',"")
        n1 = n1.replace(']',"")
        n1 = n1.replace("'","")
        entero = "Direccion de " + nombre2+": "+n1 + "\n"
        act.append(str(entero))

        tel1 = db.run("MATCH (p:Place) WHERE p.nombre = '"+nombre2+"' RETURN p.telefono").to_ndarray()
        n1 = str(tel1)
        n1= n1.replace('[',"")
        n1 = n1.replace(']',"")
        n1 = n1.replace("'","")
        entero = "Telefono de " + nombre2+": "+n1 + "\n"
        act.append(str(entero))

        if len(rec) == 3:
            dir1 = db.run("MATCH (p:Place) WHERE p.nombre = '"+nombre3+"' RETURN p.direccion").to_ndarray()
            n1 = str(dir1)
            n1= n1.replace('[',"")
            n1 = n1.replace(']',"")
            n1 = n1.replace("'","")
            entero = "Direccion de " + nombre3+": "+n1 + "\n"
            act.append(str(entero))

            tel1 = db.run("MATCH (p:Place) WHERE p.nombre = '"+nombre3+"' RETURN p.telefono").to_ndarray()
            n1 = str(tel1)
            n1= n1.replace('[',"")
            n1 = n1.replace(']',"")
            n1 = n1.replace("'","")
            entero = "Telefono de " + nombre3+": "+n1 + "\n"
            act.append(str(entero))

    
    result = verificar(act)
    return result
    
