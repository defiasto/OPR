lst = [0,1,2,3,4,5,6,7,8,9]

def summs(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + summs(lst[1::])

def rev(lst):
    if len(lst) == 1:
        return lst
    else:
        lst = rev(lst[1::]) + [lst[0]]
        return lst

def search(lst, a):
    if len(lst) == 0:
        return -1
    if lst[-1] == a:
        return len(lst)-1
    return search(lst[:-1:], a)
    
print('a)для суммирования элементов списка - summs(lst);\nb)для обращения строки - rev(lst)\nc)для последовательного поиска - search(lst,a)')
