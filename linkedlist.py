class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class Linkedlist:
   def __init__(self):
     self.head = None
   def insert(self , newNode):
      if self.head is None:
         self.head=newNode
      else:
          lastNode=self.head
          while True:
              if lastNode.next is None:
                break
              lastNode=lastNode.next
          lastNode.next = newNode
   def printList(self):
       currentNode=self.head
       while True:
           if currentNode is None:
             break
           print(currentNode.data)
           currentNode=currentNode.next
         
firstNode=Node("teja")
linkedlist=Linkedlist()
linkedlist.insert(firstNode)
secondNode=Node("dhivya")
linkedlist.insert(secondNode)
linkedlist.printList()
    
