i, s, n, m = 1, 0, 123456789, 4
while i <= m:
	s += n // (10 ** (i - 1)) % 10
	i += 1
	
print(s)