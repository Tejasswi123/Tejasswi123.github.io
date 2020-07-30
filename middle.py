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
        temp=self.head
        count=0
        while(self.head):
          if (count&1):
            temp=temp.next
          self.head=self.head.next
          count=count+1
        print(temp.data)
firstNode=Node("teja")
linkedlist=Linkedlist()
linkedlist.insert(firstNode)
secondNode=Node("dhivya")
linkedlist.insert(secondNode)
thirdNode=Node("dhana")
linkedlist.insert(thirdNode)



linkedlist.printList()
    
