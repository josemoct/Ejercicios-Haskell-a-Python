# -*- coding: utf-8 -*-
def factorial(num):
    facto=1
    for i in range(1,num+1):
        facto=facto*i
    return facto

numero=input("Ingrese el número")
print(repr(numero)+"! es igual a "+repr(factorial(numero)))
