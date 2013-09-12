def gcd(m, r):
	if r == 0:
		return m
	return gcd(r, m % r)
	
def gcd3(a, b, c):
	return gcd(gcd(a, b), c)
	
print(gcd3(45, 15, 10))