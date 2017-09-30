

arreglo = [1,2,3,"hola",1.8]

#los siguientes dos for son lo mismo, unicamente es diferente sintaxis

for element in range(0, len(arreglo)):
	print(arreglo[element])
	break

for element in arreglo:
	print(element)
	break

#con el brake rompemos el ciclo del for
# y solo nos devolveria el primer elemento
#aplica para el FOR y el WHILE
for element in range(0, len(arreglo)):
	print(element)