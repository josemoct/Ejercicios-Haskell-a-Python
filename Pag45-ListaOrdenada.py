# -*- coding: utf-8 -*-
from __future__ import unicode_literals

lista=[]
print "Llenaras una lista de 5 elementos y Comprobaremos si esta ordenada"
for i in range(0,5):
	lista.append(raw_input("Elemento: "))
condicion = True
i=0
while i<len(lista):
        for j in range(i+1,len(lista)):
                if lista[i]>lista[j]:
                        condicion=False
        i+=1
 
if condicion:
        print "La lista esta ordenada"
else:
        print "La lista no esta ordenada"
