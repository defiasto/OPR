ap = [1,0,3,1,2,3,3]
i, s, p = 0, 0, 4

while i < len(ap):
	s += ap[i] * (p ** i)
	i += 1
	
print(s)