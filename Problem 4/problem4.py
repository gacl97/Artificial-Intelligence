from random import randrange
from Tree import *
from Node import *

x = randrange(3)
y = randrange(3)
firstTable = [[-1]*3 for i in range(3)]
game = Tree()
print("----------- welcome to the tic-tac-toe game -----------")
print()
print("[1] - Player 1 (X)")
print("[2] - Player 2 (O)")
print()
print("-------------------------------------------------------")
print()
# aux = [[1,-1,1],[0,0,-1],[0,1,1]]
# table = game.createNode(0,0,aux,1)
# game.printTable(table.table)
# totalPoints = 0
# totalPoints += game.validateDiagonal(table,0)
# totalPoints -= game.validateDiagonal(table,1)
# totalPoints += game.validateRow(table,0)
# totalPoints += game.validateColumn(table,0)
# totalPoints -= game.validateRow(table,1)
# totalPoints -= game.validateColumn(table,1)
# print(totalPoints)

gameTable = game.createNode(x,y,firstTable,1)
game.printTable(gameTable.table)
game.generateNode(gameTable)