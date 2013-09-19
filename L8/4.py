s = "A very long string with many spacessdsd adn literals"
i, max, temp = 0, 0, 0
out = True
word, tword = "", ""

while i < len(s):
	if i == len(s) - 1:
		temp += 1
		tword += s[i]
		if temp >= max:
			max, word = temp, tword
			tword, temp = "", 0
		else:
			tword, temp = "", 0
	elif s[i] != " ":
		temp += 1
		tword += s[i]	
	else:
		if temp >= max:
			max, word = temp, tword
			tword, temp = "", 0
		else:
			tword, temp = "", 0
	i += 1
print(word)		