def century(n):
	if n > 0:
		return (n - 1) // 100 + 1
	elif n == 0:
		return "Error"
	else:
		return ((abs(n) - 1) // 100 + 1) * -1
