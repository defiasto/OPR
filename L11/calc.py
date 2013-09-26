from tkinter import *

def calculate(e, l):
	a = e.get().split("+")
	n = 0
	for i in a:
		n += int(i)
	l["text"] = str(n)

root = Tk()
ent = Entry(root, width=50, bd=3, text="1+1")
lab = Label(root, text="Result")
but = Button(root, text="Calculate!", command = lambda: calculate(ent, lab))
ent.pack()
lab.pack()
but.pack()
root.mainloop()