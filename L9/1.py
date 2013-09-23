i = 0
x = str(123456)
a = []
while i < len(x):
	a.append(int(x[i]))
	i += 1
print(a[::-1])