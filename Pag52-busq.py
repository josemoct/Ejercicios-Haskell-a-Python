# -*- coding: utf-8 -*-
def busq(lista,num):  #Devuelve el elemento ubicado en la posicion n
    for i in range(0,len(lista)):
        if i==num:
            n=lista[i]
    return n

lista=[]
tam=input("Ingrese el tamaño de la lista")
for i in range(0,tam):
    lista.append(raw_input("Ingrese el elemento "+repr(i+1)))
n=input("Ingrese la posición a buscar")
print ("El elemento en la posición "+repr(n)+" es igual a "+repr(busq(lista,n)))

