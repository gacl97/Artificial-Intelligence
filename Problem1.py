class Node:


  def __init__(self, qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2):
    self.side1 = [qnt_m1, qnt_c1]
    self.boat = [qnt_mb, qnt_cb]
    self.side2 = [qnt_m2,qnt_c2]
    self.sons = []

class Tree:

  def createNode(self, qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2):
    return Node(qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2)

  def boarding(self, currentSide, currentNode):

    #Verificar o lado atual se negativo lado 1 se positivo lado 2
    if (not currentSide):

      #Embarcar um Canibal e um Missionario 
      if (currentNode.side1[0] - 1 >= (currentNode.side1[1] - 1) and currentNode.side1[0] - 1 >= 0 and currentNode.side1[1] - 1 >= 0):
        print("Um de cada")
        newNode = self.createNode(currentNode.side1[0]-1,currentNode.side1[1]-1,1,1,currentNode.side2[0],currentNode.side2[1])
        currentNode.sons.append(newNode)

      #Mandar somente um canibal
      if (currentNode.side1[1] - 1 >= 0 and currentNode.side1[0] >= currentNode.side1[1] - 1):
        print("Um canibal")
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1]-1,0,1,currentNode.side2[0],currentNode.side2[1])
        currentNode.sons.append(newNode)

      #Mandar dois canibais 
      if (currentNode.side1[1] - 2 >= 0 and currentNode.side1[0] >= currentNode.side1[1] - 2):
        print("Dois canibais")
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1]-2,0,2,currentNode.side2[0],currentNode.side2[1])
        currentNode.sons.append(newNode)
    else:

      #Embarcar um Canibal e um Missionario 
      if (currentNode.side2[0] - 1 >= currentNode.side2[1] - 1 and currentNode.side2[0] - 1 >= 0 and currentNode.side2[1] - 1 >= 0):
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],1,1,currentNode.side2[0]-1,currentNode.side2[1]-1)
        currentNode.sons.append(newNode)
      #Mandar somente um canibal
      if (currentNode.side2[1] - 1 >= 0 and currentNode.side2[0] >= currentNode.side2[1] - 1):
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,1,currentNode.side2[0],currentNode.side2[1]-1)
        currentNode.sons.append(newNode)
      #Mandar dois canibais 
      if (currentNode.side2[1] - 2 >= 0 and currentNode.side2[0] >= currentNode.side2[1] - 2):
        newNode = self.createNode(currentNode.side1[0],currentNode.side1[1],0,2,currentNode.side2[0],currentNode.side2[1]-2)
        currentNode.sons.append(newNode)
  

  def landing(self, currentSide, currentNode):

    print()
    print ("Lado 1: ")
    print()
    print("Qnt Missionario: ", currentNode.side1[0], "Qnt Canibal: ", currentNode.side1[1])
    print("Barco: ")
    print("Qnt Missionario: ", currentNode.boat[0], "Qnt Canibal: ", currentNode.boat[1])
    print("Destino: ")
    print("Qnt Missionario: ", currentNode.side2[0], "Qnt Canibal: ", currentNode.side2[1])
    print()
    if (not currentSide):
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

    else:

      print("Descer no lado dois")
      print()
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


tree = Tree()
root = Node(3,3,0,0,0,0)
tree.boarding(False,root)
tree.landing(True,root.sons[0])
tree.landing(True,root.sons[1])
tree.landing(True,root.sons[2])
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