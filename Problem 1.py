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

      if (boat[0] == 0 and boat[1] == 0):

        #Embarcar um Canibal e um Missionario
        if (side1[0] - 1 >= side1[1] - 1):
          
        newNode = createNode(2,2,1,1,0,0)
        self.sons.append(newNode)
        newNode = createNode(2,2,0,1,0,0)
        self.sons.append(newNode)
        newNode = createNode(2,2,0,2,0,0)
        self.sons.append(newNode)
      elif (boat[0] == 1 and boat[1] == 0 or boat[0] == 0 and boat[1] == 1):
        
        #Mandar um missionario somente se a qnt dele for maior que canibais
        if (side1[0] - 1 >= 0 and side1[0] - 1 >= side1[1]):
          
          #newNode = createNode()
        elif (side1[1] - 1 >=0 ):
          #Mandar um canibal 
          #newNode = createNode()
  
  def landing(self, currentSide):

    if (currentSide):

      #Chegando um Missionario e um Canibal
      if (boat[0] == 1 and boat[1] == 1):
        
        #Verificar se é possível descer
        if (side2[0] + 1 >= side2[1] + 1):

          newNode = createNode(self.side1[0],self.side1[1],0,0,self.side2[0]+1, self.side2[1]+1)
          self.sons.append(newNode)

      #Chegando apenas um canibal
      elif (boat[0] == 0 and boat[1] == 1):
        
        #Verificar se é possível a descida do canibal
        if (side2[1] + 1 >= side2[0]):
          newNode = createNode(self.side1[0],self.side1[1],0,0,self.side2[0], self.side2[1]+1)
          self.sons.append(newNode)

      #Chegando dois canibais
      elif (boat[0] == 0 and boat[1] == 2):

        #Verificar se é possível a descida dos dois canibais
        if (side2[1] + 2 >= side2[0]):
          newNode = createNode(self.side1[0],self.side1[1],0,0,self.side2[0], self.side2[1]+2)
          self.sons.append(newNode)

    else:

      #Chegando um Missionario e um Canibal
      if (boat[0] == 1 and boat[1] == 1):
        
        #Verificar se é possível descer
        if (side1[0] + 1 >= side1[1] + 1):

          newNode = createNode(self.side1[0]+1,self.side1[1]+1,0,0,self.side2[0], self.side2[1])
          self.sons.append(newNode)

      #Chegando apenas um canibal
      elif (boat[0] == 0 and boat[1] == 1):
        
        #Verificar se é possível a descida do canibal
        if (side1[1] + 1 >= side1[0]):
          newNode = createNode(self.side1[0],self.side1[1]+1,0,0,self.side2[0], self.side2[1])
          self.sons.append(newNode)

      #Chegando dois canibais
      elif (boat[0] == 0 and boat[1] == 2):

        #Verificar se é possível a descida dos dois canibais
        if (side1[1] + 2 >= side1[0]):
          newNode = createNode(self.side1[0],self.side1[1]+2,0,0,self.side2[0], self.side2[1])
          self.sons.append(newNode)

    

    


  
    

root = node()
root.createNode(3,3,0,0,0,0)
newNode = createNode(2,2,1,1,0,0)
root.sons.append(newNode)
newNode = createNode(2,2,0,1,0,0)
root.sons.append(newNode)
newNode = createNode(2,2,0,2,0,0)
root.sons.append(newNode)