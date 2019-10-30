class node:

  sons = []
  side1 = [0]*2
  boat = [0]*2
  side2 = [0]*2

  def createNode(self, qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2):
    self.side1[0] = qnt_m1
    self.side1[1] = qnt_c1
    self.boat[0] = qnt_mb
    self.boat[1] = qnt_cb
    self.side2[0] = qnt_m2
    self.side2[1] = qnt_c2

  def boarding(self, currentSide):

    #Verificar o lado atual se negativo lado 1 se positivo lado 2
    if (not currentSide):
      #Embarcar um Canibal e um Missionario 
      if (self.side1[0] - 1 >= (self.side1[1] - 1) and self.side1[0] - 1 >= 0 and self.side1[1] - 1 >= 0):
        newNode = self.createNode(self.side1[0]-1,self.side1[1]-1,1,1,self.side2[0],self.side2[1])
        self.sons.append(newNode)
        print(self.side1[1])
      #Mandar somente um canibal
      if (self.side1[1] - 1 >= 0 and self.side1[1] - 1 >= self.side1[0]):
        print("CHE")
        newNode = self.createNode(self.side1[0],self.side1[1]-1,0,1,self.side2[0],self.side2[1])
        self.sons.append(newNode)
      #Mandar dois canibais 
      if (self.side1[1] - 2 >= 0 and self.side1[1] - 2 >= self.side1[0]):
        newNode = self.createNode(self.side1[0],self.side1[1]-2,0,2,self.side2[0],self.side2[1])
        self.sons.append(newNode)

    else:

      #Embarcar um Canibal e um Missionario 
      if (self.side2[0] - 1 >= self.side2[1] - 1 and self.side2[0] - 1 >= 0 and self.side2[1] - 1 >= 0):
        newNode = self.createNode(self.side1[0],self.side1[1],1,1,self.side2[0]-1,self.side2[1]-1)
        self.sons.append(newNode)
      #Mandar somente um canibal
      if (self.side2[1] - 1 >= 0 and self.side2[1] - 1 >= self.side2[0]):
        newNode = self.createNode(self.side1[0],self.side1[1],0,1,self.side2[0],self.side2[1]-1)
        self.sons.append(newNode)
      #Mandar dois canibais 
      if (self.side2[1] - 2 >= 0 and self.side2[1] - 2 >= self.side2[0]):
        newNode = self.createNode(self.side1[0],self.side1[1],0,2,self.side2[0],self.side2[1]-2)
        self.sons.append(newNode)


  def landing(self, currentSide):

    if (currentSide):

      #Chegando um Missionario e um Canibal
      if (self.boat[0] == 1 and self.boat[1] == 1):
        
        #Verificar se é possível descer
        if (self.side2[0] + 1 >= self.side2[1] + 1):

          newNode = self.createNode(self.side1[0],self.side1[1],0,0,self.side2[0]+1, self.side2[1]+1)
          self.sons.append(newNode)

      #Chegando apenas um canibal
      if (self.boat[0] == 0 and self.boat[1] == 1):
        
        #Verificar se é possível a descida do canibal
        if (self.side2[1] + 1 >= self.side2[0]):
          newNode = self.createNode(self.side1[0],self.side1[1],0,0,self.side2[0], self.side2[1]+1)
          self.sons.append(newNode)

      #Chegando dois canibais
      if (self.boat[0] == 0 and self.boat[1] == 2):

        #Verificar se é possível a descida dos dois canibais
        if (self.side2[1] + 2 >= self.side2[0]):
          newNode = self.createNode(self.side1[0],self.side1[1],0,0,self.side2[0], self.side2[1]+2)
          self.sons.append(newNode)

    else:

      #Chegando um Missionario e um Canibal
      if (self.boat[0] == 1 and self.boat[1] == 1):
        
        #Verificar se é possível descer
        if (self.side1[0] + 1 >= self.side1[1] + 1):

          newNode = self.createNode(self.side1[0]+1,self.side1[1]+1,0,0,self.side2[0], self.side2[1])
          self.sons.append(newNode)

      #Chegando apenas um canibal
      if (self.boat[0] == 0 and self.boat[1] == 1):
        
        #Verificar se é possível a descida do canibal
        if (self.side1[1] + 1 >= self.side1[0]):
          newNode = self.createNode(self.side1[0],self.side1[1]+1,0,0,self.side2[0], self.side2[1])
          self.sons.append(newNode)

      #Chegando dois canibais
      if (self.boat[0] == 0 and self.boat[1] == 2):

        #Verificar se é possível a descida dos dois canibais
        if (self.side1[1] + 2 >= self.side1[0]):
          newNode = self.createNode(self.side1[0],self.side1[1]+2,0,0,self.side2[0], self.side2[1])
          self.sons.append(newNode)

root = node()
root.createNode(3,3,0,0,0,0)
root.boarding(False)
#newNode = root.createNode(2,2,1,1,0,0)
#root.sons.append(newNode)
#newNode = createNode(2,2,0,1,0,0)
#root.sons.append(newNode)
#newNode = createNode(2,2,0,2,0,0)
#root.sons.append(newNode)
for i in root.sons:
  print ("AQU")