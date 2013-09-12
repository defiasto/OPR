def fac(n):
	i = 1
	fac = 1
	while i <= n:
		fac *= i
		i += 1
	return fac
	
i = 1
res = 0
while i <= 10:
	res += fac(i)
	i += 1
	
print(res)