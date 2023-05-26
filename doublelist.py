class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None #setting both the left and right pointers as none
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def insertLeft(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
        else:
            n.right=self.head   #first we set the right of n to point to head
            self.head.left=n   #then setting the left of head to point to n
            self.head=n       #then setting the inserted element as new head

    def deleteLeft(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head              #storing the head in a temp variable
            self.head=self.head.right  #we will set the element to the right of the head as new head
            self.head.left=None      #then we will set left of the new head as none so the element will get deleted
            print(f"Deleted Data: {temp.data}")    

    def insertRight(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
        else:
            temp=self.head             #first store the head in a temp variable
            while (temp.right!=None):  #we will travers till the end of the list
                temp=temp.right       #insert the new element to the right of the temp
            temp.right=n             #set the left of the new node to point to temp
            n.left=temp
    
    def deleteRight(self):
        if self.head==None:
            print("List is empty")
        else:
            t=self.head
            while(t.right!=None):
                t=t.right
            if t==self.head:
                self.head=None
            else:
                t2=t.left
                t2.right=None
                print(f"Deleted Data: {t.data}")
    
    def printReverse(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while(temp.right!=None):       #first we will traverse till the end of the list
                temp=temp.right
            while(temp!=None):                     
                print(f"|{temp.data}|-->",end='')  #once we reach the end we will go on pointing to left of temp and print each node
                temp=temp.left
    
    def search(self,key):
        count=0
        if self.head==None:
            print("List is Empty")
        else:
            temp=self.head
            while(temp.right!=None):
                count += 1
                if (temp.data==key):
                    return print(f"{key} found at position {count} ")
                temp=temp.right
            return(f"{key} not found")

    def deleteKey(self,key):
        if self.head==None:
            print("List is empty")
        else:
            t=t2=self.head
            while(t!=None and t.data!=key):  #we will keep traversing the list till there is a match for the key  as soon as there is a match for the key the condition in the while loop will become false and it will come out of the loop
                t2=t
                t=t.right
            if t!=None:
                if t==self.head:
                    self.head=self.head.right
                    self.head.left=None
                elif t.right==None:
                    t2.right=None
                else:
                    t2.right=t.right


    def printList(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while(temp!=None):
                print(f"|{temp.data}|-->",end='')
                temp=temp.right

    
objdouble=DoubleLinkedList()
while True:
    print(f" 1.Insert Left \n 2.Insert Right \n 3.Delete Left \n 4.Delete Right \n 5.Search key \n 6.Delete key \n 7.Print list \n 8.Print Reverse \n 9.Exit")
    ch=float(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter data: "))
        objdouble.insertRight(data)
    elif ch==2:
        data=int(input("Enter data: "))
        objdouble.insertleft(data)
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