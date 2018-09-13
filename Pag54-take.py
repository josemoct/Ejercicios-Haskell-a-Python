# -*- coding: utf-8 -*-
def take(lista,num):   #Retorna los primeros n elementos de la lista
    listaAux=[]
    for i in range(0,num):
        listaAux.append(lista[i])
    return listaAux

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento " + repr(i + 1)))
n=input("Ingrese los n elementos que desea obtener")
print ("Lista de los primeros "+repr(n)+" elementos:"+repr(take(lista,n)))