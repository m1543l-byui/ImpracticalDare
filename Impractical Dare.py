"""
Author: Misael Payan
Class: CSE 310
Brother McBeth
Sprint 1 - Impractical Dare
"""
import random

# Input players 
players = []

# Set new_player to something other than 'start'.
new_player = ''

# Start a loop that will run until the user enters 'start'.
while new_player != 'start', or 'Start', or 'START':
    # Ask the user for a name.
    new_player = input("Enter player name, or enter 'start' to begin the game: ")

    # Add the names to our list.
    players.append(new_player)

# Remove the start from the player list
if "start" in new_player:
    players.pop()

# Show that the name has been added to the list.
print()
print(players)

# Select a DARE file, once selected, the program will cycle through the list 
# and select a random dare for the players to perform.
def random_dare(dare):
    lines = open(dare).read().splitlines()
    lines.pop()
    return random.choice(lines)

print()
print("Your Challenge is: ")
print(random_dare('dares1.txt'))
print()

# Set player points
player_points = {players[0]:0, players[1]:0, players[2]:0, players[3]:0}

# Keep track of score
for player in players:
    if input(f"Did {player} complete the challenge? (y/n) ") == 'y' or 'Y':
        player_points[player] += 1
print()

for player in players:
    print(f"{player} has a score of {player_points[player]}")
print()

