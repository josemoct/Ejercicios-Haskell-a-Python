# -*- coding: utf-8 -*-
def fibonacci(num):
    n1=0
    n2=1
    for i in range(1,num):
        t=n1+n2
        n1=n2
        n2=t
    return n2

numero=input("Ingrese el número")
print (repr(numero)+" termino de la serie de fibonacci es "+repr(fibonacci(numero)))