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

#Test Scenario 3 Bug: Pass erroneous array as parameter to testUtility.getCurseCards in order to introduce bug that
#changes the number of curse cards presented in the game.
testArray = ["val1", "val2", "val3", "val4", "val5", "val6"]

nC = testUtility.getCurseCards(testArray)

#Define box
box = testUtility.getBoxes(nV)

supply_order = testUtility.getSupplyOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.getRandomSupply(box)

#The supply always has these cards
testUtility.setSupply(supply, player_names, nV, nC)

#Test Scenario 2 Bug: Change value of Silver in supply to simulate a bug in the data set resulting in additional Copper
#with incorrect supply output to players.
supply["Silver"] = [Dominion.Copper()] * 40

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers(player_names)

# Play the game
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
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
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
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
