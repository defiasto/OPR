def sum(x):
	i,s = 0, 0
	while i < len(x):
		s += x[i]
		i += 1
	return s
	
a = [[1,2,3],[3,2,2],[1,1,1]]

a.sort(key = sum)

print(a)