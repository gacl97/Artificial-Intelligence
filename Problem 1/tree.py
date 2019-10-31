from node import *

class Tree:

    def createNode(self, qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2, flag, prev):
        return Node(qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2, flag, prev)

    def compare(self, node1, node2):
        if(node1.side1[0] == node2.side1[0] and node1.side1[1] == node2.side1[1] and node1.side2[0] == node2.side2[0] and node1.side2[1] == node2.side2[1] and node1.boat[0] == node2.boat[0] and node1.boat[1] == node2.boat[1]):
            return False
        else:
            return True

    def print1(self, currentNode):
        if(currentNode == None):
            return
        self.print1(currentNode.prev)
        if (currentNode.prev == None):
            print("------------------------------------")
            print("Qnt Missionario: ", currentNode.side1[0], "Qnt Canibal: ", currentNode.side1[1])
            print("Barco: ")
            print("Qnt Missionario: ", currentNode.boat[0], "Qnt Canibal: ", currentNode.boat[1])
            print("Destino: ")
            print("Qnt Missionario: ", currentNode.side2[0], "Qnt Canibal: ", currentNode.side2[1])
            print("------------------------------------")
            return
        if(not currentNode.flag):
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", end = "\n\n")
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", end = "\n\n")
        if(currentNode.boat[0] == 1 and currentNode.boat[1] == 1):
            print("Embarca 1 missionario e 1 canibal")
        elif(currentNode.boat[0] == 0 and currentNode.boat[1] == 2):
            print("Embarca 2 canibais")
        elif(currentNode.boat[0] == 2 and currentNode.boat[1] == 0):
            print("Embarca 2 missionarios")
        elif(currentNode.boat[0] == 1 and currentNode.boat[1] == 0):
            print("Embarca 1 missionario")
        else:
            print("Embarca 1 canibal")
        print()
        print("Qnt Missionario: ", currentNode.side1[0], "Qnt Canibal: ", currentNode.side1[1])
        print("Barco: ")
        print("Qnt Missionario: ", currentNode.boat[0], "Qnt Canibal: ", currentNode.boat[1])
        print("Destino: ")
        print("Qnt Missionario: ", currentNode.side2[0], "Qnt Canibal: ", currentNode.side2[1])
        print()

    def boarding(self, currentNode):
        #Embarque do lado esquerdo
        if(not currentNode.flag):
            mis = currentNode.side1[0] + currentNode.boat[0]
            can = currentNode.side1[1] + currentNode.boat[1]
            # Mandar 1 canibal e 1 missionario
            if (mis >= can and mis >= 1 and can >= 1):
                newNode = self.createNode(mis - 1, can - 1, 1, 1, currentNode.side2[0], currentNode.side2[1], not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            #Mandar 2 missionarios
            if(mis == 2 or (mis - 2 >= can and mis >= 2)):
                newNode = self.createNode(mis - 2, can, 2, 0, currentNode.side2[0], currentNode.side2[1], not currentNode.flag, currentNode)
                if(self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            #Mandar 2 canibais
            if(can >= 2):
                newNode = self.createNode(mis, can - 2, 0, 2, currentNode.side2[0], currentNode.side2[1], not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            # Mandar 1 missionario
            if ((mis >= 1 and mis - 1 >= can) or mis == 1):
                newNode = self.createNode(mis - 1, can, 1, 0, currentNode.side2[0], currentNode.side2[1],
                                          not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            # Mandar 1 canibal
            if(can >= 1):
                newNode = self.createNode(mis, can - 1, 0, 1, currentNode.side2[0], currentNode.side2[1], not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)

        # Embarque do lado direito
        else:
            mis = currentNode.side2[0] + currentNode.boat[0]
            can = currentNode.side2[1] + currentNode.boat[1]
            # Mandar 1 canibal e 1 missionario
            if (can >= 1):
                newNode = self.createNode(currentNode.side1[0], currentNode.side1[1], 0, 1, mis, can - 1,
                                          not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            # Mandar 2 missionarios
            if (mis == 2 or (mis - 2 >= can and mis >= 2)):
                newNode = self.createNode(currentNode.side1[0], currentNode.side1[1], 2, 0, mis - 2, can, not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            # Mandar 2 canibais
            if (can >= 2):
                newNode = self.createNode(currentNode.side1[0], currentNode.side1[1], 0, 2, mis, can - 2, not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            # Mandar 1 missionario
            if ((mis >= 1 and mis - 1 >= can) or mis == 1):
                newNode = self.createNode(currentNode.side1[0], currentNode.side1[1], 1, 0, mis - 1, can, not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)
            # Mandar 1 canibal
            if (mis >= can and mis >= 1 and can >= 1):
                newNode = self.createNode(currentNode.side1[0], currentNode.side1[1], 1, 1, mis - 1, can - 1, not currentNode.flag, currentNode)
                if (self.compare(newNode, currentNode)):
                    currentNode.sons.append(newNode)

    def generateStates(self, begin):
        queue = []
        queue.append(begin)
        while(len(queue) != 0):
            x = queue.pop(0)
            #Se chegar num movimento inválido (Mais canibais que missionários)
            if(x.flag == False and (x.side1[0] + x.boat[0] <  x.side1[1] + x.boat[1] and x.side1[0] + x.boat[0] > 0)):
                continue
            elif(x.flag == True and (x.side2[0] + x.boat[0] <  x.side2[1] + x.boat[1] and x.side2[0] + x.boat[0] > 0)):
                continue
            if(x.side2[0] + x.boat[0] == 3 and x.side2[1] + x.boat[1] == 3):
                self.print1(x)
                self.print1(Node(0, 0, 0, 0, 3, 3, False, None))
                break
            self.boarding(x)
            for currentSon in x.sons:
                queue.append(currentSon)