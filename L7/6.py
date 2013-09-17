a = [1,2,3,5,6]
b = 2

for i in a:
	if (b >= i) and (b <= a[a.index(i) + 1]):
		a.insert(a.index(i) + 1, b)
		break
		
print(a)