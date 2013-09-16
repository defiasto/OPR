def zip(a, b):
	if len(a) != len(b):
		return 0
	i = 0
	c = []

	while i < len(a):
		c.append([a[i], b[i]])
		i += 1
	return c
		
print(zip([1, 2, 3], ["a", "b", "c"]))