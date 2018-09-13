# -*- coding: utf-8 -*-
def head(lista):   #Devuelve la cabeza de la lista
    return lista[0]

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento " + repr(i + 1)))
print ("La cabeza de la lista es "+repr(head(lista)))