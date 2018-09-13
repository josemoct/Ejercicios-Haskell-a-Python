# -*- coding: utf-8 -*-
def length(lista):  #Retorna el número de elementos de la lista
    for i in range(0,len(lista)):
        n=i+1
    return n

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento " + repr(i + 1)))
print ("La lista tiene "+repr(length(lista))+" elemento(s)")