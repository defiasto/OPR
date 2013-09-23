a = {"ada":1980, "fortran":1957, "c":1972, "lisp":1958,
	"python":1991, "perl":1987, "java":1995, "pascal":1970,
	"haskell":1990, "erlang":1987}

k = sorted(a.keys())
c = []

for i in k:
	c.append(str(a[i]) + "\t" +i)
c.sort()
for i in c:
	print(i)