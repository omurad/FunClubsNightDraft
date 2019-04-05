import Tkinter as tk
import tkSimpleDialog
import math
from random import randint

players = []

def draft ():
	playerCount = 0;
	# Put all the players into an array
	for line in text.get('1.0', 'end-1c').splitlines():
		if line:
			players.append("@"+line)
			playerCount += 1
			
	text.pack_forget()
	draftBtn.pack_forget()
	
	# How many teams to split players into?
	teams = tkSimpleDialog.askstring("How many teams?", "How many teams to draft?", parent=main, minvalue=0)
	
	#players per team
	ppt = math.floor(playerCount / int(teams))
	remainder = playerCount % int(teams)
	remainderAssigned = 0
	print "ppt="+str(ppt)
	
	col = 0
	# Display Draft
	for i in range(int(teams)):
		currentTeam = ""
		# Create a random team of ppt players
		for z in range(int(ppt)):
			index = randint(0, len(players)-1)
			print len(players)
			currentTeam += players[index]+"\n"
			del players[index]
	
		# Add remainder players if necessary
		if remainderAssigned != remainder:
			index = randint(0, len(players)-1)
			currentTeam += players[index]+"\n"
			remainderAssigned += 1
	
		tk.Label(main, text="Team "+str(i+1)).grid(column=col, row=0)
		teamBox = tk.Text(main, width=40)
		teamBox.insert(tk.END, currentTeam)
		teamBox.grid(column=col, row=1)
		
		# Reset temp var
		del teamBox
		
		col += 1
		
		

main = tk.Tk()

text = tk.Text(main)
draftBtn = tk.Button(main, text="Draft!", width = 75, command=draft)

text.pack()
draftBtn.pack()

text.focus_set()

main.mainloop()
