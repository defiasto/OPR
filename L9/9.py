a = ["kill", "me", "pls", "it", "is", "midnight", "already", "kill", "pls"]
b = {}
for i in a:
	if i not in b:
		b[i] = 1
	else:
		b[i] += 1
		
print(b)