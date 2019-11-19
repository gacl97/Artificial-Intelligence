class Node:

    def __init__(self, x, y, lastTable, item):
        self.lastTable = lastTable
        for i in range(3):
            for j in range(3):
                self.lastTable[i][j] = lastTable[i][j]
        self.table = [[0]*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.table[i][j] = lastTable[i][j]
        self.table[x][y] = item