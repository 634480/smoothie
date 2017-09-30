maxi = int(input("ingresa un numero"))
mini = int(input("ingresa un numero"))
temp = 0
if maxi < mini:
	temp = maxi
	maxi = mini
	mini = temp

counter = 0

while True:
	counter =+ 1
	if mini  != maxi:
		mini += 1
		