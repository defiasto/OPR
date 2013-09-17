temp = 1
n, m = 5, 3

def fac(x):
	if x > 1:
		return x * fac(x - 1)
	else:
		return x

for i in range((n - m + 1), n + 1):
	temp *= i
	
print(temp / fac(m))