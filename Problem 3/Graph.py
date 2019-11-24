import random
from Node import *

class Graph:

    flag = True
    hamiltonian_path = []
    visited = [0]*11

    def create_node(self, id1, depth, prev_node):
        return Node(id1,depth,prev_node)

    def print_best_path(self, best_path):
        print("----------- The best way is -----------")
        print()
        for i in range(len(best_path)):
            if(i + 1 == len(best_path)):
                print(best_path[i].id)
                break
            print(best_path[i].id, " -> ", end="")
        print()

    # Função recebe novo caminho e verifica se o caminho está correto
    def check_path(self, graph, new_hamiltonian_path):
        
        for i in range(1,len(new_hamiltonian_path)):
            flag = False
            for j in graph[new_hamiltonian_path[i-1].id]:
                if(new_hamiltonian_path[i].id == j.id):
                    flag = True
                    break
            if(not flag):
                return False
        return True

    def get_total_cost(self, new_hamiltonian_path, distances):
        total = 0
        for i in range(1,len(new_hamiltonian_path)):
            total += distances[new_hamiltonian_path[i-1].id-1][new_hamiltonian_path[i].id-1]
        return total

    def hill_climbing(self, graph, distances):
        new_hamiltonian_path = []
        for i in self.hamiltonian_path:
            new_hamiltonian_path.append(i)
        
        best_path = []
        best_cost = 99999999

        for i in range(600000):
            x = random.randint(1,9)
            y = random.randint(1,9)
            new_hamiltonian_path[x],new_hamiltonian_path[y] = new_hamiltonian_path[y],new_hamiltonian_path[x]
            # Se o caminho for verdadeiro, verificar se é o melhor
            if(self.check_path(graph,new_hamiltonian_path) == True):

                current_cost = self.get_total_cost(new_hamiltonian_path,distances)
                if(current_cost < best_cost):
                    best_path.clear()
                    best_path = [0]*len(new_hamiltonian_path)
                    for i in range(len(new_hamiltonian_path)):
                        best_path[i] = new_hamiltonian_path[i]
                    best_cost = current_cost 
    
        self.print_best_path(best_path)
        print("Cost: ", best_cost)

    def get_hamiltonian_path(self, node, first):

        current_node = node
        while(current_node.id != first):
            self.hamiltonian_path.insert(0,current_node)
            current_node = current_node.prev_node
        self.hamiltonian_path.insert(0,current_node)

    def dfs(self, graph, begin, first):

        self.visited[begin.id] = 1
        if(begin.depth == 9 and self.flag):
            self.flag = False
            self.hamiltonian_path.append(self.create_node(first,0,begin))
            self.get_hamiltonian_path(begin,first)
            return
        for i in graph[begin.id]:

            if (not self.visited[i.id]):
                i.depth = begin.depth + 1
                i.prev_node = begin
                if(self.flag):
                    self.dfs(graph,i,first)
                self.visited[i.id] = 0
        
    def createGraph(self, distances, fileAdjList):
            graph = []
            graph.append([])

            for i in range(10):
                adjList = []
                for j in fileAdjList.readline().split():
                   adjList.append(self.create_node(int(j),0,""))
                graph.append(adjList)
            return graph

def readDistances(distances):
    dist = []
    for i in range(10):
        dist.append(list(map(int,distances.readline().split())))
    return dist