# -*- coding: utf-8 -*-
def drop(lista,num):    #Retorna los elementos de la lista excepto los n primeros
    listaAux=[]
    for i in range(num,len(lista)):
        listaAux.append(lista[i])
    return listaAux

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento " + repr(i + 1)))
n=input("Ingrese los n elementos que desea obtener")
print ("Lista sin los primeros "+repr(n)+" elementos:"+repr(drop(lista,n)))