a = [1, 1, 1, 1, 1]
i = 0
a[0] += 1

while i < len(a):
	if a[i] == 2:
		a[i] = 0
		try:
			a[i + 1] += 1
		except:
			a.append(1)
	i += 1	
	
print(a)