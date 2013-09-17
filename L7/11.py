def spllst(a):
	b, c = [], []
	for i in a:
		if i % 2:
			c.append(i)
		else:
			b.append(i)
	return b, c

a = [1,2,3,4,5,6,7,8,9]	
print(spllst(a))