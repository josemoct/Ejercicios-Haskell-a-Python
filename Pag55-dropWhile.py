lista=[]
listaAux=[]
print "Elige el numero limite inferior y el superior de una lista"
lim_inferior=input("Limite inferior: ")
lim_superior=input("Limite superior: ")

for i in range(lim_inferior,lim_superior+1):
	lista.append(i)

limite = input("Escribe el numero limite para tomar solo sus mayores ")

for numero in lista:
    if numero>limite:
        listaAux.append(numero)
if listaAux==null:
        print "Tus rangos no coinciden"
else:
        print "La lista con numeros mayores a",limite,"es ahora: ",listaAux
