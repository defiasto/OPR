i = 1
n = 10
res = 0
while i <= n:
	if i % 2:
		res += i
	else:
		res -= i
	i += 1
		
print(res)