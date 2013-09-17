a = [1,2,3,4,5,4,3,3,2,1,1]
b = []
for i in a:
	if not i in b:
		b.append(i)
		
print(b)