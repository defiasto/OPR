n, m = 6, 4
a, b, c = 0, 0, 0

def gcd(m, r):
	if r == 0:
		return m
	return gcd(r, m % r)
	
x = gcd(max(n, m), min(n, m))

if x > 1:
	n, m = n // x, m // x
	
if n > m:
	c = n // m
	a, b= n - m * c, m
else:
	a, b, c = n, m, 0

if a:	
	print(c, a, b)
else:
	print(c)