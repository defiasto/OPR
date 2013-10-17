def cond(a, i):
    if i % 2 and a != 1:
        for j in range(2, int(a ** 0.5) + 1):
            if a % j == 0:
                return False
        return True
    else:
        return False
                       
def search(lst, cond):
    for i in(range(len(lst))):
        if cond(lst[i], i):
            return i
    return -1
