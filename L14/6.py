def make_str(a, s):
    if a == 0:
        lst = s.split()
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        return lst
    else:
        stroka = ''
        for i in range(0,21):
            stroka += str(s[i]) + ' '
        return stroka

def mini(lst, r):
    a = r
    while r < len(lst) - 1:
        if lst[r + 1] < lst[a]:
            a = r + 1
        r += 1
    return a

def sort_sel(lb):
    r = 0
    lst = make_str(0, lb['text'])
    while r != len(lst):
        m = mini(lst, r)
        lst[r], lst[m] = lst[m], lst[r]
        lb['text'] = make_str(1, lst)
        root.update_idletasks()
        sleep(0.5)
        r += 1

def bubble_sort(lb):
    lst = make_str(0, lb['text'])
    for i in range(len(lst)):
        boolean = True
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1],lst[j]
                lb['text'] = make_str(1, lst)
                root.update_idletasks()
                sleep(0.5)
                boolean = False
        if boolean:
            break
    
def rep(s):
    lst = make_str(0, s)
    for i in range(0, 21):
        r = randint(0, 20)
        lst[i], lst[r] = lst[r], lst[i]
    return make_str(1, lst)
    
from tkinter import *
from random import randint
from time import *
root = Tk()
var = IntVar()
var.set(0)
rad1 = Radiobutton(root, text='Пузырьковая сортировка', variable=var, value=0)
rad2 = Radiobutton(root, text='Сортировка выборкой   ', variable=var, value=1)
rad1.grid(column=1, row=1)
rad2.grid(column=1, row=2)
stroka = ''
for i in range(0, 21):
    stroka += str(i) + ' '
lb = Label(text=stroka, font='Arial 20')
lb.grid(column=2, row=3)
mix = Button(text='Перемешать')
mix.grid(column=1,row=4)
sort = Button(text='Сортировать')
sort.grid(column=3,row=4)

def f(e):
    lb['text'] = rep(lb['text'])

def d(e):
    if var.get() == 0:
        bubble_sort(lb)
    else:
        sort_sel(lb)
    
mix.bind('<Button-1>', f)
sort.bind('<Button-1>', d)
root.mainloop()