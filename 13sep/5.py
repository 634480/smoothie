text = input ("dame un texto \n")




a = "a"
c_a = 0 
for letter in text:
	if letter in a:
		c_a += 1

e = "e"
c_e = 0 
for letter in text:
	if letter in e:
		c_e += 1

i = "i"
c_i = 0 
for letter in text:
	if letter in i:
		c_i += 1

o = "o"
c_o = 0 
for letter in text:
	if letter in o:
		c_o += 1

u = "u"
c_u = 0 
for letter in text:
	if letter in u:
		c_u += 1



print ('hay', c_a, 'a en: ', text, "\n",'hay', c_e, 'e en: ', text, "\n", 'hay', c_i, 'i en: ', text, "\n",'hay', c_o, 'o en: ', text, "\n",'hay', c_u, 'u en: ', text, "\n",)