class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
      def __init__(self):
         self.head=None
      def listprint(self):
         val=self.head
         while val is not None:
            print(val.data)
            val=val.next
list=linkedlist()
list.head=Node("mon")
e2=Node("tue")

list.head.next=e2
list.listprint()
           
