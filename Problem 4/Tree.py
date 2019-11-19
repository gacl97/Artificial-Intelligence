from Node import *

class Tree():

    def createNode(self, x, y, lastTable, item):
        return Node(x,y,lastTable,item)

    def icon(self, item):
        
        if(item == -1):
            return " "
        elif(item == 1):
            return "X"
        else:
            return "O"

    def printTable(self, table):
        
        print("   0      1     2")
        print()
        for i in range(3):
            for j in range(3):
                item = self.icon(table[i][j])
                if(j == 2):

                    print(" ",item)
                    break
                if(j == 1):
                    print(" ",item, " |", end="")
                    continue
                print(i," ",item, " |", end="")

            if(i == 2):
                break
            print("  -----|-----|-----")
        print()

    def checkVictory(self, currentNode, item):
        # Verificar linha sendo item o valor que quer verificar
        for i in range(3):
            flag = True
            for j in range(3):
                if(currentNode.table[i][j] != item):
                    flag = False
            if(flag):
                return True
        #Verificar diagonal 1
        flag = True
        for i in range(3):
            for j in range(3):
                if(i + j == 2):
                    if(currentNode.table[i][j] != item):
                        flag = False
                        break
        if(flag):
            return True
        flag = True
        # Diagonal 2
        for i in range(3):
            for j in range(3):
                if(i == j):
                    if(currentNode.table[i][j] != item):
                        flag = False
                        break
        if(flag):
            return True
        # Coluna
        for i in range(3):
            flag = True
            for j in range(3):
                if (currentNode.table[j][i] != item):
                    flag = False
            if(flag):
                return True
        count = 0
        for i in range(3):
            for j in range(3):
                if(currentNode.table[i][j] == -1):
                    count += 1
        if(count > 0):
            return False
        else:
            return True
    def exception(self, currentNode):
        while True:
            try:
                print("Your turn: ")
                print()
                print("Choose row index from [0-2]")
                x = int(input())
                print("Choose column index from [0-2]")
                y = int(input())

                if (x >= 0 and x <= 2 and y >= 0 and y <= 2 and currentNode.table[x][y] == -1):
                    return self.createNode(x,y,currentNode.table,0)
            except:
                pass
            print("Chosen values already used or out of indexes")

    def totalPoints(self, count):

        if (count == 1):
            return 1
        elif(count == 2):
            return 10
        elif(count == 3):
            return 100
        return 0

    def validateRow(self, state, item):
        # Para verificar X item deve ser igual a 0
        points = 0
        for i in range(3):
            count = 0
            for j in range(3):
                # Se não é um espaço vazio e é o item proibido
                if (state.table[i][j] != -1 and state.table[i][j] == item):
                    count -= 10000
                    break
                # Se não for espaço vazio é o item certo
                if(state.table[i][j] != -1):
                    count += 1
            points += self.totalPoints(count)
        return points

    def validateColumn(self, state, item):

        # Colunas
        points = 0
        for i in range(3):
            count = 0
            for j in range(3):
                # Se não é um espaço vazio e é o item proibido
                if(state.table[j][i] != -1 and state.table[j][i] == item):
                    count -= 10000
                    break
                # Se não for espaço vazio é o item certo
                if (state.table[j][i] != -1):
                    count += 1
            
            points += self.totalPoints(count)
        return points
    
    def validateDiagonal(self, state, item):

        points = 0
        flag = False
        for i in range(3):
            count = 0
            for j in range(3):
                 if(i+j == 2):
                    # Se não é um espaço vazio e é o item proibido
                    if(state.table[i][j] != -1 and state.table[i][j] == item):
                        count -= 10000
                        flag = True
                        break
                    # Se não for espaço vazio é o item certo
                    if (state.table[i][j] != -1):
                        count += 1
            if(flag):
                points = 0
                break
            points += self.totalPoints(count)
        flag = False
        for i in range(3):
            count = 0
            for j in range(3):
                # Se não é um espaço vazio e é o item proibido
                if(i == j):
                    if(state.table[i][j] != -1 and state.table[i][j] == item):
                        count -= -10000
                        flag = True
                        break
                    # Se não for espaço vazio é o item certo
                    if (state.table[i][j] != -1):
                        count += 1
            if(flag):
                points = 0
                break
            points += self.totalPoints(count)
        return points

    def generateNode(self, currentNode):

        while((not self.checkVictory(currentNode,1) or self.checkVictory(currentNode,0))):
            playerNode = self.exception(currentNode)
            print("--- PLAYER 1 ---")
            print()
            self.printTable(playerNode.table)
            print("--- Player 2 ---")
            print()
            if(self.checkVictory(currentNode,1) or self.checkVictory(currentNode,0)):
                break
            AiNode = self.generateStates(playerNode)
            self.printTable(AiNode.table)
            currentNode = AiNode
            print()

    def generateStates(self, currentNode):

        states = []
        for i in range(3):
            for j in range(3):
                totalPoints = 0
                if(currentNode.table[i][j] == -1):
                    newNode = self.createNode(i,j,currentNode.table,1)
                    totalPoints += self.validateDiagonal(newNode,0)
                    totalPoints -= self.validateDiagonal(newNode,1)
                    totalPoints += self.validateRow(newNode,0)
                    totalPoints += self.validateColumn(newNode,0)
                    totalPoints -= self.validateRow(newNode,1)
                    totalPoints -= self.validateColumn(newNode,1)
                    states.append([newNode,totalPoints])

        betterPoints = -1
        betterNode = ""
        for i in states:
            
            if(i[1] > betterPoints):
                betterPoints = i[1]
                betterNode = i[0]
        return betterNode