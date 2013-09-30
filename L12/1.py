from tkinter import *
# Using dictionary here to store external variables
ext = {"p": 1, "m": 0, "ms": [0, 0, 0, 0, 0, 0, 0, 0, 0]}

# Checks if the game has ended
def endgame(e):
	if e["ms"][0] == e["ms"][1] == e["ms"][2]:
		return e["ms"][0]
	elif e["ms"][3] == e["ms"][4] == e["ms"][5]:
		return e["ms"][3]
	elif e["ms"][6] == e["ms"][7] == e["ms"][8]:
		return e["ms"][6]
	elif e["ms"][0] == e["ms"][3] == e["ms"][6]:
		return e["ms"][0]
	elif e["ms"][0] == e["ms"][1] == e["ms"][2]:
		return e["ms"][0]
	elif e["ms"][1] == e["ms"][4] == e["ms"][7]:
		return e["ms"][1]
	elif e["ms"][0] == e["ms"][1] == e["ms"][2]:
		return e["ms"][0]
	elif e["ms"][2] == e["ms"][5] == e["ms"][8]:
		return e["ms"][2]
	elif e["ms"][0] == e["ms"][4] == e["ms"][8]:
		return e["ms"][0]
	elif e["ms"][2] == e["ms"][4] == e["ms"][6]:
		return e["ms"][2]
	elif e["m"] == 9:
		return "DROW"
	else:
		return False

# P1 and P2 moves are processed with this function		
def mkmove(x, e, l, b):
	if not endgame(e) and e["ms"][x - 1] == 0:
		if e["p"] == 1:
			b.config(text = "X")
			e["ms"][x - 1] = 1
			e["p"] *= -1
			e["m"] += 1
		else:
			b.config(text = "O")
			e["ms"][x - 1] = 2
			e["p"] *= -1
			e["m"] += 1
			
	if endgame(e) == 1:
		l["text"] = "X win!"
	elif endgame(e) == 2:
		l["text"] = "O win!"
	elif endgame(e) == "DROW":
		l["text"] = "Drow"


# Interface description
root = Tk()
l1 = Label(root, text = "MOVE!")
b1 = Button(root, text = "", command = lambda:mkmove(1, ext, l1, b1), width = 5)
b2 = Button(root, text = "", command = lambda:mkmove(2, ext, l1, b2), width = 5)
b3 = Button(root, text = "", command = lambda:mkmove(3, ext, l1, b3), width = 5)
b4 = Button(root, text = "", command = lambda:mkmove(4, ext, l1, b4), width = 5)
b5 = Button(root, text = "", command = lambda:mkmove(5, ext, l1, b5), width = 5)
b6 = Button(root, text = "", command = lambda:mkmove(6, ext, l1, b6), width = 5)
b7 = Button(root, text = "", command = lambda:mkmove(7, ext, l1, b7), width = 5)
b8 = Button(root, text = "", command = lambda:mkmove(8, ext, l1, b8), width = 5)
b9 = Button(root, text = "", command = lambda:mkmove(9, ext, l1, b9), width = 5)

b1.grid(row = 1, column = 1)
b2.grid(row = 1, column = 2)
b3.grid(row = 1, column = 3)
b4.grid(row = 2, column = 1)
b5.grid(row = 2, column = 2)
b6.grid(row = 2, column = 3)
b7.grid(row = 3, column = 1)
b8.grid(row = 3, column = 2)
b9.grid(row = 3, column = 3)
l1.grid(row = 4, columnspan = 3)
root.wm_title("Tic-Tac-Toe")
root.mainloop()
