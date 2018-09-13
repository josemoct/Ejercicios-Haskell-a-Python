# -*- coding: utf-8 -*-
def init(lista):   #Retorna todo los elementos menos el ultimo
    listaAux=[]
    for i in range(0,len(lista)-1):
        listaAux.append(lista[i])
    return listaAux

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento " + repr(i + 1)))
print ("Lista sin el último elemento:"+repr(init(lista)))