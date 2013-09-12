# I use gcd() here to count lcm()
def gcd(m, r):
	if r == 0:
		return m
	return gcd(r, m % r)
	
def lcm(a, b):
	return abs(a * b)//gcd(a, b)
	
print(lcm(16, 8))