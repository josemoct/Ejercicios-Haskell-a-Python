# -*- coding: utf-8 -*-
from __future__ import unicode_literals

lista=[]
print "Llenaras una lista de 5 elementos para luego decirte el mayor de esa lista"

for i in range(0,5):
	lista.append(raw_input("Elemento: "))

numero_mayor=lista[0]
for numero in lista:
	if(numero>numero_mayor):
		numero_mayor=numero

print "El elemento mayor de la lista es:",numero_mayor		
