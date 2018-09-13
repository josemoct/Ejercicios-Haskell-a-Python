# -*- coding: utf-8 -*-
from __future__ import unicode_literals

lista=[]
print "Llenaras una lista de 5 numeros para luego devolver sus numeros al cuadrado"

for i in range(0,5):
	lista.append(input("Numero: "))

print "Tu lista ahora al cuadrado: "
for i in lista:
	print i*i