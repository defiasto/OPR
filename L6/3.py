word = "matanatam"

def isPalindrome(x):
	if word == word[::-1]:
		return True
	else:
		return False
	
print(isPalindrome(word))