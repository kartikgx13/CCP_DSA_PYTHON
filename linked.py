class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        n=Node(data)
        if self.head==None:  
            self.head=n
        else:
            temp=self.head #3-> 
            while temp!=None:
                temp=temp.next
            temp.next=n




 


        