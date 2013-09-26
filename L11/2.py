# You should type "34 in 2" to see 34 in binary

from tkinter import *

def i2s(n, p):
	s = ''
	while n:
		d = n % p
		s = str(d) + s
		n = n // p
	return s
	
def transform(e, l):
	a = e.get().split(" in ")
	l["text"] = i2s(int(a[0]), int(a[1]))
	
	
root = Tk()
ent = Entry(root, width=50, bd=3, text="1+1")
lab = Label(root, text="Result")
but = Button(root, text="Transform!", command = lambda: transform(ent, lab))
ent.pack()
lab.pack()
but.pack()
root.mainloop()