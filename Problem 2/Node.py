class Node:

    def __init__(self, id1, heuristDist, dist, prevColor):
        self.id = id1
        self.heuristDist = heuristDist
        self.dist = dist
        self.prevColor = prevColor

    def savePrevNode(self, prevNode):
        self.prevNode = prevNode
        
    def saveCost(self, cost):
        self.cost = cost