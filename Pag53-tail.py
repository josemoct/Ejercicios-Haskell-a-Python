# -*- coding: utf-8 -*-
def tail(lista):  #Retorna todos los elementos menos el primero
    listaAux=[]
    for i in range(1,len(lista)):
        listaAux.insert(i-1,lista[i])
    return listaAux

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento " + repr(i + 1)))
print ("Lista sin cabeza:"+repr(tail(lista)))