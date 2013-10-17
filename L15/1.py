def isLetter(a):
    if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z'):
        return True
    else:
        return False

def isName(s):
    if len(s) == 1:
        return isLetter(s)
    else:
        if isLetter(s[0]):
            return isName(s[1::])
        else:
            return False
