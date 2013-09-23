### THE CODE DOESN'T WORK. IT HAS FUCKING BUGS
"""
a, b = [1, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1]
A, B, c = [], [], []

if len(a) > len(b):
	A, B = a[::-1], b[::-1]
else:
	A, B = b[::-1], a[::-1]
	
for i in A:
	try:
		c.append(A[i] + B[i])
	except:
		c.append(A[i])

i = 0		
while i < len(c):
	if c[i] == 2:
		c[i] = 0
		try:
			c[i + 1] += 1
		except:
			c.append(1)
	
	i += 1
		
print(c[::-1])
"""