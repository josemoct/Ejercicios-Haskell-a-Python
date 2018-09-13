# -*- coding: utf-8 -*-
from __future__ import unicode_literals

numero_max = input("Escribe hasta donde quieres que genere los numeros primos")
numero=1
while(numero<numero_max):
	contador = 0
	for i in range(2,numero_max):
		if numero%i == 0:
			contador+=1

	if contador<2:
		print "El numero ",numero," es primo"
		print contador
	numero+=1
