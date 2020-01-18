# -*- coding: utf-8 -*-
"""
Created on Tue January 15th, 2020

@author: Justin Tromp
"""

import Dominion

#Get player names
from projects.trompj.dominion import testUtility

player_names = testUtility.getPlayerNames()

#number of curses and victory cards
nV = testUtility.getVictoryCards(player_names)

nC = testUtility.getCurseCards(player_names)

#Define box
box = testUtility.getBoxes(nV)

#Test Scenario 1 Data Change/Bug: Change value of Woodcutter in box to simulate a bug in the data set resulting in
#no Gardens in box and 2 extra Woodcutters.
del box["Gardens"]
box["Woodcutter"] = [Dominion.Gardens()] * nV

supply_order = testUtility.getSupplyOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.getRandomSupply(box)


#The supply always has these cards
testUtility.setSupply(supply, player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers(player_names)

#Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name,player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)
            

#Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
