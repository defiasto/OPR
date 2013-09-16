a = [-1, 2, -3, 4, -5, 6]

for i in a:
	if i < 0:
		del(a[a.index(i)])
		
print(a)