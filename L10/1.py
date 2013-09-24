f1 = open("f1.txt", "a")
f2 = open("f2.txt", "r")

f1.writelines(f2.readlines())
f1.close()
f2.close
	