# -*- coding: utf-8 -*-
from __future__ import unicode_literals
lista=[]
listaCambiada=[]
print "Llenaras una lista de 5 numeros sumaremos sus numeros"
for i in range(0,5):
	lista.append(input("Numero: "))

suma_numeros=0
for numero in lista:
	suma_numeros+=numero

print suma_numeros
