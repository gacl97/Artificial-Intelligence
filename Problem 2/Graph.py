from Node import *
from queue import PriorityQueue
class graph:

    colors = [-1, [0,0],[0,1],[0,3],[0,2],[0,1],[0,0],[1,1],[1,2],[1,3],[1,1],[3,3],[2,2],[2,3],[2,2]]

    def createNode(self, id1, heuristDist, dist, prevColor):
        return Node(id1,heuristDist,dist,prevColor)

    def createGraph(self, distances, end, fileAdjList):
        graph = []
        graph.append([])
        # Azul = 0 Amarelo = 1 Verde = 2 Vermelho = 3
        for i in range(14):
            adjList = []
            for j in fileAdjList.readline().split():
                adjList.append(self.createNode(int(j),distances[int(j)-1][end-1],distances[i][int(j)-1],""))
            graph.append(adjList)
        return graph
    
    def printGraph(self):

        
        for i in range(15):
            print(i,"-> ", end="")
            for j in graph[i]:
                print(j.id, " ", end="")
            print()

    def searchCommonColor(self, prev, current):

        for i in self.colors[prev]:
            for j in self.colors[current.id]:
                if(i == j):
                    current.prevColor = i
                    break
            
    def printPath(self,node):

        if(node.prevNode.id == node.id):
            print("----------- The best way is -----------")
            print()
            print("Passing by the station ",node.id, "with the cost ", node.dist)
        else:
            self.printPath(node.prevNode)

            if (node.prevColor == 0):
                color = "blue"    
            elif(node.prevColor == 1):
                color = "yellow"
            elif(node.prevColor == 2):
                color = "green"
            else:
                color = "red"
            print("Passing by the station ",node.id, "with the cost ", node.cost, "by the line ", color)

    def bestPath(self, begin, end, graph, dist):

        visited = [0]*15
        queue = PriorityQueue()
        count = 0
        for i in graph[begin]:
            self.searchCommonColor(begin,i)
            currentDist = i.dist + i.heuristDist
            visited[i.id] = 1
            aux = self.createNode(begin,dist[begin-1][end-1],0,"")
            aux.savePrevNode(aux)
            i.savePrevNode(aux)
            i.saveCost(currentDist)
            queue.put([currentDist,i.id,begin,count])
            count += 1
        # print()
        while(not queue.empty()):
            currentNode = queue.get()
            visited[currentNode[1]] = 1

            if (currentNode[1] == end):
                graph[currentNode[2]][currentNode[3]].saveCost(currentNode[0])
                self.printPath(graph[currentNode[2]][currentNode[3]])
                print("Final cost = ", currentNode[0])
                break
            count = 0
            for node in graph[currentNode[1]]:

                if(visited[node.id] == 0):

                    self.searchCommonColor(currentNode[1],node)
                    node.savePrevNode(graph[currentNode[2]][currentNode[3]])
                    if(graph[currentNode[2]][currentNode[3]].prevColor != node.prevColor):
                        currentDist = currentNode[0] + node.dist + node.heuristDist + 2
                    else:
                        currentDist = currentNode[0] + node.dist + node.heuristDist
                    node.saveCost(currentDist)
                    queue.put([currentDist,node.id,currentNode[1],count])
                count += 1


def readDistances(distances):
    dist = []
    for i in range(14):
        dist.append(list(map(int,distances.readline().split())))
    return dist