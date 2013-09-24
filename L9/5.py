def sums(x, y):
	z = []
	if len(x) < len(y):
		x, y = y, x
	i, t = 0, 0
	while i < len(x):
		if i == len(y):
			y.append(0)
		t = t + x[i] + y[i]
		z.append(t % 2)
		t = t // 2
		i += 1
	while t!=0:
		z.append(t % 2)
		t = t // 2
	return z
	
a, b = [0, 0, 1, 1], [1, 1, 1, 1, 0, 1]
print(sums(a, b))
# Written by Stas