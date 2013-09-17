# True > False, lol.
def sign(x):
	if x >= 0:
		return True
	else:
		return False
		
a = [1,-2,3,-4,-1,2,-3,4]
a.sort(key = sign)
print(a)