# -*- coding: utf-8 -*-
from __future__ import unicode_literals
lista=[]
listaCambiada=[]
print "Llenaras una lista de 5 elementos y le daremos la vuelta"
for i in range(0,5):
	lista.append(raw_input("Elemento: "))


for i in range(1,len(lista)+1):
	listaCambiada.append(lista[len(lista)-i])

print listaCambiada
