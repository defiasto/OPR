a = [1,2,3,4]
b = [3,5,1]

for i in a:
	if i in b:
		a.remove(i)
		
print(a)