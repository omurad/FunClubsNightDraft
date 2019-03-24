import random

print "A file named players.txt must exist in the same directory as this script.\n"

# How many teams
teamCount = input("Number of teams: ")

# Put all players into array
with open('players.txt') as file:
    players = file.readlines()

# Strip newlines
for i, player in enumerate(players):
    players[i] = player.strip()

# Create file for each team
for i in range(1, teamCount+1):
	open("team"+str(i)+".txt","w+")
	
# Loop over players
team = 1
for i in range (0, len(players)):
	# Pick random player from current draft
	draftNum = random.randrange(0, len(players))
	
	# Append player to team file
	with open("team"+str(team)+".txt", "a") as file:
		file.write("@"+players[draftNum]+"\n")
		
	# Remove selected player from draft list
	del players[draftNum]
	
	# Make sure team variable doesn't go beyond the specified team count
	if team == teamCount:
		team = 1
	else:
		team = team + 1
