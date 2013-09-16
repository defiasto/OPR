a = [1, 2, 3, 4, 5, 6]

def sum(x):
	i,s = 0, 0
	while i < len(x):
		s += x[i]
		i += 1
	return s
	
print(sum(a))