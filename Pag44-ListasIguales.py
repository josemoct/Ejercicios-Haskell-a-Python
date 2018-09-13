# -*- coding: utf-8 -*-
from __future__ import unicode_literals

lista1=[]
lista2=[]
print "Llenaras la primera lista de 5 elementos y se compara con la segunda que llenaras luego"
for i in range(0,5):
	lista1.append(raw_input("Elemento: "))
print "Ahora llena la segunda lista: "
for i in range(0,5):
	lista2.append(raw_input("Elemento: "))

listasSonIguales=True
for i in range(0,5):
    if lista1[i]!=lista2[i]:
        listasSonIguales=False



if listasSonIguales:
	print "Son iguales"
else:
	print "No son iguales"
