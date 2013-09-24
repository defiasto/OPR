f = open("f3.txt", "r")
max = ''
s = f.readlines()

for i in s:
	if len(i) > len(max):
		max = i

print(i)

f.close()