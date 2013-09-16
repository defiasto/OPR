n = int(input(''))
m = int(input(''))
i = 1
s = 0
x = 0
if n > m:
	while i <= m:
		x = n % 10
		s += x
		n = n // 10
		i += 1
else :
	m = len(n)
	while i <= m:
		x = n % 10
		s += x
		n = n // 10
		i += 1
print (s)