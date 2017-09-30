

variable =int(input("ingresa en valor "))

variable2 =int(input("ingresa un valor menor al anterior "))


if variable > variable2:
	c = 0
	while variable != variable2:
	    variable2 = variable2 + 1
	    c = c + 1
	    variable =- 1
	    c = c + 1

else:
    print(c)



