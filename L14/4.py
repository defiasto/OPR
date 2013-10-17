def bubble_sort(lst):
    for i in range(len(lst)):
        boolean = True
        for j in range(len(lst)- i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                boolean = False
        if boolean:
            break