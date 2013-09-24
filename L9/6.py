def setun(n):
	a = ['0', '1', 'i']
	b = ''
	while n:
		d = n % 3
		if d == 2:
			n = n + 3
		b = a[d] + b
		n = n // 3
	return n
	
print(setun(56))