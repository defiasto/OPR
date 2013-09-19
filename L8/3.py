def dummy(x):
	pass
	
def count(n):
	i = 1
	while True:
		try:
			dummy(n[i])
			i += 1
		except:
			break
	return i
	
def find(x, y):
	for i in x:
		if y == i:
			return x.index(i)
	return -1

a = [1,2,3,4,5,6,7]
print(count(a))
print(find(a, 2))