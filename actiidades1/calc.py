#Calculadora de cajita de cereal
def sumar(x,y):
    return (x + y)

def restar(x,y):
    return (x - y)

def multiplicar(x,y):
    return (x * y)

def dividir(x,y):
    return (x / y)

def raiz(x):
    return (x**0.5)


#solicitar al usuario operacion y cantidades
print(" ")
print("¿Que operacion quieres realizar?")
print("Ingresa el numero de la opcion deseada")
print(" ")
print("Sumar ---------- 1")
print("Restar --------- 2")
print("Multiplicar ---- 3")
print("Dividir -------- 4")
print(" ")

op = int(input())



x = int(input("Ingresa primer numero "))
y = int(input("Ingresa segundo numero "))

if op ==1:
	print (sumar (x,y))

elif op ==2:
	print (restar (x,y))

elif op ==3:
	print (multiplicar (x,y))

elif op ==4:
	print (dividir (x,y))




