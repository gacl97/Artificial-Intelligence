from Node import * 
from Graph import *

def exception():
    while True:
        try:
            number = int(input())
            if (number >= 1 and number <= 14):
                return number
        except:
            pass
        print("Invalid station, please choose again from [1-14]")


graphInstance = graph()
fileDistances = open('distances.txt', 'r')
dist = readDistances(fileDistances)
fileDistances.close()
fileAdjList = open('adj_list.txt','r')
print("--------- Welcome to Paris subway ---------")
print()
print("Which station [1-14] will you depart from: ")
begin = exception()
print("And at which station will you land: ")
end = exception()
graph = graphInstance.createGraph(dist,end,fileAdjList)
fileAdjList.close() 
print()
graphInstance.bestPath(begin,end,graph, dist)