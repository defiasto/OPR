def mini(lst,r):
    a = r
    while r < len(lst) - 1:
        if lst[r + 1] < lst[a]:
            a = r + 1
        r += 1
    return a

def sort_sel(lst):
    r = 0
    while r != len(lst):
        m = mini(lst, r)
        lst[r], lst[m] = lst[m], lst[r]
        r += 1
