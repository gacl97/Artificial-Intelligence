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
            count = 0
            for j in range(3):
                # Se possuir uma linha inteira completa
                if(currentNode.table[i][j] == item):
                    count += 1
            if(count == 3):
                return False
        #Verificar diagonal 1
        count = 0
        for i in range(3):
            for j in range(3):
                if(i + j == 2):
                    if(currentNode.table[i][j] == item):
                        count += 1
        if(count == 3):
            return False
        # Diagonal 2
        count = 0
        for i in range(3):
            for j in range(3):
                if(i == j):
                    if(currentNode.table[i][j] == item):
                        count += 1
        if(count == 3):
            return False
        # Coluna
        for i in range(3):
            count = 0
            for j in range(3):
                if (currentNode.table[j][i] == item):
                    count += 1
            if(count == 3):
                return False
        count = 0
        for i in range(3):
            for j in range(3):
                if(currentNode.table[i][j] == -1):
                    count += 1
        if(count > 0):
            return True
        else:
            return False

    def exception(self, currentNode):
        while True:
            try:
                print("Your turn: ")
                print()
                print("Choose row and column index from [0-2]")
                x,y = input().split()
                x = int(x)
                y = int(y)
                # Validar posições e retornar um estado caso válido
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



    def winner(self, player1, player2):
        if (not(player1) and not(player2)):
            print("EMPATE")
            return
        if(player1):
            print("PlAYER 1 WIN!!!")
        elif(player2):
            print("PLAYER 2 WIN!!!")

    def generateNode(self, currentNode):
        
        while True:
            flag1 = self.checkVictory(currentNode,1)
            flag2 = self.checkVictory(currentNode,0)
            if (not(flag1 and flag2)):
                self.winner(flag1,flag2)
                break
            player2Node = self.exception(currentNode)
            print("--- PLAYER 1 ---")
            print()
            self.printTable(player2Node.table)
            # Verificar se já possui um ganhador
            flag1 = self.checkVictory(currentNode,1)
            flag2 = self.checkVictory(currentNode,0)
            if(not(flag1) or not(flag2)):
                self.winner(flag1,flag2)
                break
            print("--------------------")
            print()
            print("--- Player 2 ---")
            print()
            player2Node = self.generateStates(player2Node)
            self.printTable(player2Node.table)
            currentNode = player2Node
            print()