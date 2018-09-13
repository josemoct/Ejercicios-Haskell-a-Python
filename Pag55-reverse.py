# -*- coding: utf-8 -*-
def reverse(lista): #Invierte el orden de una lista
    listaAux=[]
    n=len(lista)-1
    for i in range(0,len(lista)):
        listaAux.append(lista[n])
        n=n-1
    return listaAux

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento "+repr(i+1)))
print ("Lista invertida:"+repr(reverse(lista)))