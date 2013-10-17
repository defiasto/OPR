def fib(i):
    if i == 1 or i == 2:
        return 1
    elif i == 0:
        return i
    return fib(i - 2) * 2 + fib(i - 3)
