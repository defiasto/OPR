def new_trian(lst, a, canva):
    if a > 0:
        cord = []
        for i in range(0, len(lst) - 2, 2):
            cord.append((lst[i] + lst[i + 2]) / 2)
            cord.append((lst[i + 1] + lst[i + 3]) / 2)
        cord.append(cord[0])
        cord.append(cord[1])
        #print(cord)
        canva.create_line(cord, fill='yellow', width=1)
        a -= 1
        root.update()
        new_trian([lst[0],lst[1],cord[0],cord[1],cord[-4],cord[-3],lst[0],lst[1]],a,canva)
        new_trian([cord[0],cord[1],lst[2],lst[3],cord[2],cord[3],cord[0],cord[1]],a,canva)
        new_trian([cord[-4],cord[-3],cord[2],cord[3],lst[-4],lst[-3],cord[-4],cord[-3]],a,canva)
    return 

from tkinter import *
root = Tk()
ent = Entry(root)
ent.pack()
bt = Button(root,text='Ввести')
bt.pack()
canva = Canvas(root, width = 600, height=600, bg='blue')
cordinaty = [10,540,300,58,590,540,10,540]
canva.create_line(cordinaty, fill='yellow', width=1)
canva.pack()
def f():
    bt['state'] = DISABLED
    new_trian(cordinaty,int(ent.get()),canva)
bt['command'] = f
root.mainloop()
