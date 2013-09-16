def isLeap(year):
	d4 = not(year % 4)
	d100 = year % 100
	d400 = not(year % 400)
	
	if (d4 and d100) or d400:
		return True
	else:
		return False

print(isLeap(2004))