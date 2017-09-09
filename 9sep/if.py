"""Te pedira dos numeros y te dejara
escoger que queres hacer con ellos.
En caso de que l opcion elegida no sea corecta te dara un error"""

x = int(input('Ingresa primer valor \n'))
y = int(input('Ingresa segundo valor \n'))

print('\nElige si quieres \na - sumarlos \nb - restarlos\nc- multiplicarlos')

z = input('\n Ingresa la opcion elegida \n')

if z == 'a':
	print(x + y)
elif z == 'b':
	print(x - y)
elif z == 'c':
	print(x * y)
else:
	print('Mal, muy mal, suerte para la proxima! \n =(')
