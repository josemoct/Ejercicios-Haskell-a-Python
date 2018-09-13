lista=[]
listaUnica=[]
print "Llenaras una lista de 5 elementos y los concatenaremos en una sola lista"
for i in range(0,5):
	lista.append(raw_input("Elemento: "))

elementoBase=""
for elemento in lista:
    elementoBase+=elemento

listaUnica.insert(0,elementoBase)
print listaUnica
