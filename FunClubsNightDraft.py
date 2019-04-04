import Tkinter as tk

players = []

def draft ():
	for line in text.get('1.0', 'end-1c').splitlines():
		if line:
			players.append(line)

main = tk.Tk()

text = tk.Text(main)
draftBtn = tk.Button(main, text="Draft!", width = 75, command=draft)

text.pack()
draftBtn.pack()

text.focus_set()

main.mainloop()