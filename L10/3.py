f = open("f4.txt", "r")
f0 = open("f5.txt", "a")

s = f.readlines()
w = []
for i in s:
	if "\n" in i:
		i = i[:-1]
	for j in i.split(" "):
		if j not in w:
			w.append(j+" ")
	
f0.writelines(w)
f.close()
f0.close()