class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None #setting both the left and right pointers as none
class CircularDoubleLinkedList:
    def __init__(self):
        self.head=self.last=None
    def insertLeft(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.last=n
        else:
            n.right=self.head   #first we set the right of n to point to head
            self.head.left=n   #then setting the left of head to point to n
            self.head=n       #then setting the inserted element as new head
            self.last.right=self.head

    def deleteLeft(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head              #storing the head in a temp variable
            if self.head==self.last:
                self.head=None
            else:
                self.head=self.head.right  #then we will set the next node as head and change the pointing of the last node to point to this new head
                self.last.right=self.head   
            print(f"Delete data is {temp.data}") 

    def insertRight(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.last=n
            self.last.right=self.head
        else:
            self.last.right=n
            self.last=n               #here we will insert to the right of the last node hence self.last is used
            self.last.right=self.head
    
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
            self.last.right=self.head
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
                temp=temp.right
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
                t=t.right
            if t!=None:   
                if t==self.head:           
                    self.head=self.head.right 
                    self.last.right=self.head
                elif t==self.last:            #here only the second case will be changed as now we will check if it matches with self.last
                    self.last=t2
                    self.last.right=self.head            
                else:                        
                    t2.right=t.right
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
                temp=temp.right
                if temp==self.head:
                    break
    
    def printReverse(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while True:       #first we will traverse till the end of the list
                temp=temp.right
                if temp.right==self.head:
                    break
            while True:                     
                print(f"|{temp.data}|-->",end='')  #once we reach the end we will go on pointing to left of temp and print each node
                temp=temp.left
                if temp.left==None:                    
                    print(f"|{temp.data}|")
                    break
                

    
objdouble=CircularDoubleLinkedList()
while True:
    print(f" 1.Insert Left \n 2.Insert Right \n 3.Delete Left \n 4.Delete Right \n 5.Search key \n 6.Delete key \n 7.Print list \n 8.Print Reverse \n 9.Exit")
    ch=float(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter data: "))
        objdouble.insertLeft(data)
    elif ch==2:
        data=int(input("Enter data: "))
        objdouble.insertRight(data)
    elif ch==3:
        objdouble.deleteLeft()
    elif ch==4:
        objdouble.deleteRight()
    elif ch==5:
        key=int(input("Enter key to be found: "))
        objdouble.search(key)
    elif ch==6:
        key=int(input("Enter key to be deleted"))
        objdouble.deleteKey(key)
    elif ch==7:
        objdouble.printList()
    elif ch==8:
        objdouble.printReverse()
    elif ch==9:
        break
    else:
        print("Invalid Choice")