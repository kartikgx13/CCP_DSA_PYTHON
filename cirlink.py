class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
class CircularLinkedList:
    def __init__(self):
        self.head=self.last=None #as initally in the circle the front and the last will coincide hence both are set to none
    
    def insertLeft(self,data):
        n=Node(data)
        if self.head==None:        #if head is none then both head and last will be set to n
            self.head=self.last=n    #since its a circular list the last will point to head again
            self.last.next=self.head
        else:
            n.next=self.head
            self.head=n
            self.last.next=self.head
    
    def deleteLeft(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            if self.head==self.last: #here also there can be 2 cases that is the element left is only the head or more elements are present
                self.head=None
            else:
                self.head=self.head.next  #then we will set the next node as head and change the pointing of the last node to point to this new head
                self.last.next=self.head
            print(f"Delete data is {temp.data}")
    
    def insertRight(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.last=n
            self.last.next=self.head
        else:
            self.last.next=n
            self.last=n               #here we will insert to the right of the last node hence self.last is used
            self.last.next=self.head  #since the last node is change we again update its pointer to point to the head
    
    def deleteRight(self):
        if self.head==None:
            print("List is empty")
        else:
            t=t2=self.head
            if self.head==self.last:
                self.head=None
            while(t!=self.last):
                t2=t
                t=t.next
            self.last=t2
            self.last.next=self.head
        print(f"Deleted data: {t.data}")
    
    def search(self,key):
        count=0
        if self.head==None:
            print("List is Empty")
        else:
            temp=self.head
            while True:
                count += 1
                if (temp.data==key):
                    return print(f"{key} found at position {count} ")
                temp=temp.next
                if temp==self.head:   #we have to break here because since we started with head node so after traversing the whole list we will come back to
                    break             #to head hence we break here to come out of the while loop
            return(f"{key} not found")
    
    def deleteKey(self,key):
        if self.head==None:
            print("List is empty")
        else:
            t=t2=self.head
            while(t!=self.last and t.data!=key):  
                t2=t
                t=t.next
            if t!=None:   
                if t==self.head:           
                    self.head=self.head.next 
                    self.last.next=self.head
                elif t==self.last:            #here only the second case will be changed as now we will check if it matches with self.last
                    self.last=t2
                    self.last.next=self.head            
                else:                        
                    t2.next=t.next
                print(f"Deleted Data: {t.data}")
            else:
                print(f"{key} not found")
            
    def printList(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while True:
                print(f"|{temp.data}|-->",end='')
                temp=temp.next
                if temp==self.head:
                    break

objcirlist=CircularLinkedList()
while True:
    print(f" 1.Insert Right \n 2.Insert Left \n 3.Delete Left \n 4.Delete Right \n 5.Search key \n 6.Delete key \n 7.Print list \n 8.Exit")
    ch=float(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter data: "))
        objcirlist.insertRight(data)
    elif ch==2:
        data=int(input("Enter data: "))
        objcirlist.insertleft(data)
    elif ch==3:
        objcirlist.deleteLeft()
    elif ch==4:
        objcirlist.deleteRight()
    elif ch==5:
        key=int(input("Enter key to be found: "))
        objcirlist.search(key)
    elif ch==6:
        key=int(input("Enter key to be deleted"))
        objcirlist.deleteKey(key)
    elif ch==7:
        objcirlist.printList()
    elif ch==8:
        break
    else:
        print("Invalid Choice")
