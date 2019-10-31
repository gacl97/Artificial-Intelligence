class Node:


  def __init__(self, qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2):
    self.side1 = [qnt_m1, qnt_c1]
    self.boat = [qnt_mb, qnt_cb]
    self.side2 = [qnt_m2,qnt_c2]
    self.sons = []

class Tree:

  def createNode(self, qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2):
    return Node(qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2)

  def print1(self, currentNode):
    print()
    print ("Lado 1: ")
    print()
    print("Qnt Missionario: ", currentNode.side1[0], "Qnt Canibal: ", currentNode.side1[1])
    print("Barco: ")
    print("Qnt Missionario: ", currentNode.boat[0], "Qnt Canibal: ", currentNode.boat[1])
    print("Destino: ")
    print("Qnt Missionario: ", currentNode.side2[0], "Qnt Canibal: ", currentNode.side2[1])
    print()

  def boarding(self, currentSide, currentNode):

    #Verificar o lado atual se negativo lado 1 se positivo lado 2
    if (not currentSide):
      print("EMBARCAR NO LADO 1")
      print()
      self.print1(currentNode)
      #Embarcar um Canibal e um Missionario 
      if (currentNode.side1[0] - 1 >= (currentNode.side1[1] - 1) and currentNode.side1[0] - 1 >= 0 and currentNode.side1[1] - 1 >= 0):
        print("Embarcar um de cada")
        newNode = self.createNode(currentNode.side1[0]-1,currentNode.side1[1]-1,1,1,currentNode.side2[0],currentNode.side2[1])
        currentNode.sons.append(newNode)

      #Mandar somente um canibal
      if (currentNode.side1[1] - 1 >= 0 and currentNode.side1[0] >= currentNode.side1[1] - 1):
        print("Embarcar um canibal")
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1]-1,0,1,currentNode.side2[0],currentNode.side2[1])
        currentNode.sons.append(newNode)

      #Mandar dois canibais 
      if (currentNode.side1[1] - 2 >= 0 and currentNode.side1[0] >= currentNode.side1[1] - 2):
        print("Embarcar dois canibais")
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1]-2,0,2,currentNode.side2[0],currentNode.side2[1])
        currentNode.sons.append(newNode)
      print()
    else:

      print("EMBARCAR NO LADO 2")
      print()
      self.print1(currentNode)
      #Embarcar um Canibal e um Missionario 
      if (currentNode.side2[0] - 1 >= currentNode.side2[1] - 1 and currentNode.side2[0] - 1 >= 0 and currentNode.side2[1] - 1 >= 0):
        print("Embarcar um de cada")
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],1,1,currentNode.side2[0]-1,currentNode.side2[1]-1)
        currentNode.sons.append(newNode)
      #Mandar somente um canibal
      if (currentNode.side2[1] - 1 >= 0 and currentNode.side2[0] >= currentNode.side2[1] - 1):
        print("Embarcar um canibal")
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,1,currentNode.side2[0],currentNode.side2[1]-1)
        currentNode.sons.append(newNode)
      #Mandar dois canibais 
      if (currentNode.side2[1] - 2 >= 0 and currentNode.side2[0] >= currentNode.side2[1] - 2):
        print("Embarcar dois canibais")
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,2,currentNode.side2[0],currentNode.side2[1]-2)
        currentNode.sons.append(newNode)
        print()

  def landing(self, currentSide, currentNode):

    
    if (not currentSide):

      print("DESEMBARCAR NO LADO 1")
      print()
      self.print1(currentNode)
      #Chegando um Missionario e um Canibal
      if (currentNode.boat[0] == 1 and currentNode.boat[1] == 1):
        
        #Verificar se é possível descer
        if (currentNode.side1[0] + 1 >= currentNode.side1[1] + 1):

          print("É possivel descer um canibal e um Missionário")

          newNode = self.createNode(currentNode.side1[0]+1,currentNode.side1[1]+1,0,0,currentNode.side2[0], currentNode.side2[1])
          currentNode.sons.append(newNode)

      #Chegando apenas um canibal
      if (currentNode.boat[1] == 1):
        
        #Verificar se é possível a descida do canibal
        if (currentNode.side1[1] + 1 <= currentNode.side1[0]):

          print("É possivel descer um canibal")
          newNode = self.createNode(currentNode.side1[0],currentNode.side1[1]+1,0,0,currentNode.side2[0], currentNode.side2[1])
          currentNode.sons.append(newNode)

      #Chegando dois canibais
      if (currentNode.boat[1] == 2):

        #Verificar se é possível a descida dos dois canibais
        if (currentNode.side1[1] + 2 <= currentNode.side1[0]):
          print("É possivel descer dois canibais")
          newNode = self.createNode(currentNode.side1[0],currentNode.side1[1]+2,0,0,currentNode.side2[0], currentNode.side2[1])
          currentNode.sons.append(newNode)

      #Descer um Missionário
      if (currentNode.boat[0] == 1):

        if (currentNode.side1[0] + 1 >= currentNode.side1[1]):
          print("É possivel descer um Missionário")
          newNode = self.createNode(currentNode.side1[0]+1,currentNode.side1[1],0,0,currentNode.side2[0], currentNode.side2[1])
          currentNode.sons.append(newNode)
      print()
    else:

      print("DESEMBARCAR NO LADO 2")
      print()
      self.print1(currentNode)
        #Chegando um Missionario e um Canibal
      if (currentNode.boat[0] == 1 and currentNode.boat[1] == 1):
        
        #Verificar se é possível descer
        if (currentNode.side2[0] + 1 >= currentNode.side2[1] + 1):
          print("É possivel descer um canibal e um Missionário")
          newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,0,currentNode.side2[0]+1, currentNode.side2[1]+1)
          currentNode.sons.append(newNode)

      #Chegando apenas um canibal
      if (currentNode.boat[1] == 1):
        
        #Verificar se é possível a descida do canibal
        if (currentNode.side2[1] + 1 <= currentNode.side2[0] or currentNode.side2[0] == 0):
          print("É possivel descer um canibal")
          newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,0,currentNode.side2[0], currentNode.side2[1]+1)
          currentNode.sons.append(newNode)

      #Chegando dois canibais
      if (currentNode.boat[1] == 2):

        #Verificar se é possível a descida dos dois canibais
        if (currentNode.side2[1] + 2 <= currentNode.side2[0] or currentNode.side2[0] == 0):
          print("É possivel descer dois canibais")
          newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,0,currentNode.side2[0], currentNode.side2[1]+2)
          currentNode.sons.append(newNode)
      
      #Descer um Missionário
      if (currentNode.boat[0] == 1):

        if (currentNode.side2[0] + 1 >= currentNode.side2[1]):
          print("É possivel descer um Missionário")
          newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,0,currentNode.side2[0]+1, currentNode.side2[1])
          currentNode.sons.append(newNode)
      print()

  def generateStates(self, currentNode, bord, land):

    self.boarding(bord,currentNode)
    #Verificar se é solução
    #Percorrer os filhos do nó atual embarcados e gerar o estado de descer do barco
    adjList = []
    adjList.append(currentNode)
    
    while (len(adjList) != 0):
      currentNode = adjList.pop(0)
      for nodeBoarding in currentNode.sons:
        #Para cada filho do nó atual, criar o estado de desembarque
        print("Criando Estado de desembarque...")
        self.landing(land,nodeBoarding)
        #Percorrer os estados de desembarque para um novo embarque
        for nodeLanding in nodeBoarding.sons:
          print("EMBARCANDO....")
          #Verificar se é solução
          if (currentNode.side2[0] == 3 and currentNode.side2[1] == 3):
            print("FINALIZADO")
            return
          else:
            adjList.append(nodeLanding)
            if (not bord): 
              bord = True
              land = False
              self.boarding(bord,nodeLanding)
              #self.generateStates(nodeLanding,True,False)
            else:
              bord = False
              land = True
              self.boarding(bord,nodeLanding)
              #self.generateStates(nodeLanding,False,True)
        print("PROXIMOOO")

    

tree = Tree()
root = Node(3,3,0,0,0,0)

tree.generateStates(root,False,True)
#tree.boarding(False,root)
#FALSE E TRUE NO PRIMEIRO
#tree.landing(True,root.sons[0])
#tree.landing(True,root.sons[1])
#tree.landing(True,root.sons[2])
"""
print()
for node in root.sons:
  print ("Lado 1: ")
  print("Qnt Missionario: ", node.side1[0], "Qnt Canibal: ", node.side1[1])
  print("Barco: ")
  print("Qnt Missionario: ", node.boat[0], "Qnt Canibal: ", node.boat[1])
  print("Destino: ")
  print("Qnt Missionario: ", node.side2[0], "Qnt Canibal: ", node.side2[1])
  print()

print("---> ", len(root.sons[0].sons))
"""