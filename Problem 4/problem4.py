from random import randrange
from Tree import *
from Node import *

x = randrange(3)
y = randrange(3)
firstTable = [[-1]*3 for i in range(3)]
game = Tree()
print("----------- welcome to the tic-tac-toe game -----------")
print()
gameTable = game.createNode(x,y,firstTable,1)
game.printTable(gameTable.table)
game.generateNode(gameTable)