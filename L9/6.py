def i2s(n, p):
	s = ''
	while n:
		d = n % p
		s = str(d) + s
		n = n // p
	return s
	
x = i2s(56, 3)

# Ну его нафиг. Еще и симметричная система. Я спать!