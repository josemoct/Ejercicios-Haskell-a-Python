# -*- coding: utf-8 -*-
from __future__ import unicode_literals

lista=[]
print "Llenaras una lista de 5 elementos y preguntaras por el elemento en cierta ubicacion"
for i in range(0,5):
	lista.append(raw_input("Elemento: "))

posicion=  input("Ahora digita una posicion en el arreglo para encontrar un Elemento: ")

while(posicion<0 or posicion>=len(lista)):
	posicion = input("No existe Elemento en esa poscion, digita nuevamente una posicion: ")

print "El elemento encontrado en",posicion,"es: ",lista[posicion]
