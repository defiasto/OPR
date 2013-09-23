a = {"ada":1980, "fortran":1957, "c":1972, "lisp":1958,
	"python":1991, "perl":1987, "java":1995, "pascal":1970,
	"haskell":1990, "erlang":1987}

k = sorted(a.keys())
for i in k:
	print(i, a[i])