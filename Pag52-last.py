# -*- coding: utf-8 -*-
def last(lista):   #Devuelve el ultimo elemento de la lista
    return lista[len(lista)-1]

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento " + repr(i + 1)))
print ("El último elemento de la lista es "+repr(last(lista)))