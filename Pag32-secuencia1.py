# -*- coding: utf-8 -*-
def secuencia1(m,n):
    listaAux=[]
    if n<m:
        return listaAux
    else :
        for i in range(m,n+1):
            listaAux.append(i)
        return listaAux

num1=input("Ingrese el extremo 1 de la lista")
num2=input("Ingrese el extremo 2 de la lista")
print ("Secuencia:"+repr(secuencia1(num1,num2)))
