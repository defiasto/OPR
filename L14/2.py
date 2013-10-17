def mini(lst):
    if lst == []:
        return -1
    imin = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[imin]:
            imin = i
    return imin

        
