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

def modulo(x,y):
    return ( x -( y * (x/y)))


#solicitar al usuario operacion y cantidades
print(" ")
print("¿Que operacion quieres realizar?")
print("Ingresa el numero de la opcion deseada")
print(" ")
print("Sumar ---------- 1")
print("Restar --------- 2")
print("Multiplicar ---- 3")
print("Dividir -------- 4")
print("Raiz cuadrada--- 5")
print("Modulo---------- 6")
print(" ")

op = int(input())

if op != 5:
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

    elif op == 6:
        print (modulo (x,y))

else:
    x = int(input("Ingresa un Numero "))
    print(raiz(x))
print ("es el resultado")