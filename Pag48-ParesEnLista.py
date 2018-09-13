# -*- coding: utf-8 -*-
from __future__ import unicode_literals

lista=[]
print "Llenaras una lista de 5 numeros y sabras cuantos numeros pares hay en ella"
for i in range(0,5):
	lista.append(input("Numero: "))

contador=0
for numero in lista:
	if numero%2 ==0:
		contador+=1

print "La cantidad de numeros pares que hay es: ",contador