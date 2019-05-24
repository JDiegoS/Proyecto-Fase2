#Hoja de Trabajo 10
#Juan Diego Solorzano 18151
#Andrea Paniagua

from py2neo import *
from neo4j import *
from numpy import *
from tkinter import *

db = Graph(password = "prueba123")


def crearUsuario(nombre, edad):
    db.run("CREATE (u:Usuario {name:'"+nombre+"', age:'"+edad+"'})")

def crearRating(nombre, lugar, leGusto):
    if leGusto == "si":
        db.run("MATCH (u:Usuario), (p:Place) WHERE u.name = '"+nombre+"' AND p.name = '"+lugar+"' CREATE (u)-[:LIKES]-> (p)")
def verificar(resul):
    resultado = "Te sugerimos visitar los siguientes lugares: \n"
    if len(resul) != 0:
        
        for i in act:
            resultado = resultado + "" + i + "\n"
        
    elif len(resul) == 0:
        resultado = "No se encontraron recomendaciones"

    
    return resultado

def recomendacion(dinero, compan, actividad):

    act = []
    nombres = db.run("MATCH (p:Place)-[:ES]->(t:Tourism) WHERE t.type = '"+actividad+"' RETURN p.name").to_ndarray()
    
    for i in nombres:
            nombres = str(nombres[i])
            nomb = nombres.replace('[',"")
            nomb1 = nomb.replace(']',"")
            nomb2 = nomb1.replace("'","")
            act.append(nomb2)

    

    doc = db.run("MATCH (p:Place)-[:TIENE]->(b:Budget) WHERE b.type = '"+dinero+"' RETURN p.name").to_ndarray()
    for i in doc:
        for x in act:
            if str(i) == "['"+str(x)+"']":
                doc = str(doc[i])
                doc1 = doc.replace('[',"")
                doc2 = doc1.replace(']',"")
                doc3 = doc2.replace("'","")
                act.append(doc3)


    doc4 = db.run("MATCH (p:Place)-[:IR]->(c:Companion) WHERE c.type = '"+compan+"' RETURN p.name").to_ndarray()
    for i in nombres:
        for x in act:
            
            if str(i) == "['"+str(x)+"']":
                doc4 = str(doc4[i])
                doc5 = doc4.replace('[',"")
                doc6 = doc5.replace(']',"")
                doc7 = doc6.replace("'","")
                act.append(doc7)
    
    result = verificar(act)
    return result
    
