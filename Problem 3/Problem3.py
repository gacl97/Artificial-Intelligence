from Graph import *

def exception():
    while True:
        try:
            number = int(input())
            if (number >= 1 and number <= 10):
                return number
        except:
            pass
        print("Invalid point, please choose again from [1-10]")

fileDistances = open('distances.txt', 'r')
dist = readDistances(fileDistances)
fileDistances.close()
fileAdjList = open('adj_list.txt','r')
graph_instance = Graph()
graph = graph_instance.createGraph(dist,fileAdjList)
fileAdjList.close()

print("--------- Welcome to traveling salesman ---------")
print()
print("What is the starting point of the traveling salesman: [1-10]")
begin = exception()
begin_node = graph_instance.create_node(begin,0,"")
graph_instance.dfs(graph,begin_node,begin)
graph_instance.hill_climbing(graph,dist)