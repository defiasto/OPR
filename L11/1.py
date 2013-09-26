from tkinter import *

def swap(b1, b2):
	b1["text"], b2["text"] = b2["text"], b1["text"]

root = Tk()
b1 = Button(root, text="b1")
b2 = Button(root, text="b2")
b1["command"] = lambda: swap(b1, b2)
b2["command"] = lambda: swap(b1, b2)
b1.pack()
b2.pack()
root.mainloop()