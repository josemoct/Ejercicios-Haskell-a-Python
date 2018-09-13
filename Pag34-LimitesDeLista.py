# -*- coding: utf-8 -*-
from __future__ import unicode_literals
lista=[]
print "Se creara una lista con desde m hasta n con incremento de i"

m=input("Ingresa m: ")
n=input("Ingresa n: ")
i=input("Ingresa i: ")

for i in range(m,n,i):
    lista.append(i)

print "Tu lista esta asi: ",lista
