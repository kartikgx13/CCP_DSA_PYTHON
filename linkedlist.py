class Node:
    def __init__(self,data):
        self.data=data         #here we are creating a class node which
        self.next=None         #will define the structure of a node 
                              #since this is a single linked list there will be data and single pointer pointing to the next node

class LinkedList:
    def __init__(self):
        self.head=None    #initally as the linked list is empty the head is set to none
    
    def insertleft(self,data):  #data is the value to be inserted
        n=Node(data)           #here we created an object of class node passing the data hence the default constructor was called hence creating a node
        if self.head==None:
            self.head=n      #so if head is empty the data value is inserted into the head
        else:
            n.next=self.head  #now the newly added node points to the previous head
            self.head=n
    
    def deleteLeft(self):
        if self.head==None:
            print("List Empty")
        else:
            temp=self.head      #storing the head which is on the left in a temp variable for deletion
            self.head=self.head.next  #here we changed the head and shifted it to the element on the right of the previous head
            print(f"Deleted Data: {temp.data}")
    
    def insertRight(self,data):
        n=Node(data)              #creating a node of that node
        if self.head==None:
            self.head=n         #if head is empty insert n as head node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next       #as long as we dont reach the tail of the list just keep skiping the elements until we reach the last node
            temp.next=n           #after we reach the end insert the new data to the right of new temp which is nothing but the tail node
    
    def deleteRight(self):
        if self.head==None:
            print("List Empty")
        else:
            t=t2=self.head         #storing the head in two variables intially t and t2
            while(t.next!=None):   #until the tail node is reached store the next variable in t and the element before in t2
                t2=t
                t=t.next
            t2.next=None       #after the t variable points to none that means we have reached the element to be deleted and therefore we will set t2.next to none to remove reference of the rightmost element
            if t==self.head:
                self.head=None
            print(f"Deleted Data: {t.data}")  #even if t.next is None it still has a data value so we print that

    def search(self,key):
        count=0
        if self.head==None:
            print("List is Empty")
        else:
            temp=self.head
            while(temp!=None):
                count += 1
                if (temp.data==key):
                    return print(f"{key} found at position {count} ")
                temp=temp.next
            return(f"{key} not found")
    
    def deleteKey(self,key):
        if self.head==None:
            print("List is empty")
        else:
            t=t2=self.head
            while(t!=None and t.data!=key):  #we will keep traversing the list till there is a match for the key  as soon as there is a match for the key the condition in the while loop will become false and it will come out of the loop
                t2=t
                t=t.next
            if t!=None:   #here the element which we want to search is now in t
                if t==self.head:        #if t is head then the element towards its right will become the new head and hence t will be deleted      
                    self.head=self.head.next #here there will be 3 cases:
                elif t.next==None:           #key is head
                    t2.next=None             #key is tail 
                else:                        #key is in between
                    t2.next=t.next
                print(f"Deleted Data: {t.data}")
            else:
                print(f"{key} not found")


    def printList(self):
        temp=self.head       #first we will store the head in a temp variable
        while temp!=None:    #continue the loop until we reach the tail
            print(f"|{temp.data}|-->",end='')
            temp = temp.next     #here temp.next will have some value until it reaches tail where its value will become None and it will come out of the while loop


objlist=LinkedList()
while True:
    print(f" 1.Insert Left \n 2.Insert Right \n 3.Delete Left \n 4.Delete Right \n 5.Search key \n 6.Delete key \n 7.Print list \n 8.Exit")
    ch=float(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter data: "))
        objlist.insertRight(data)
    elif ch==2:
        data=int(input("Enter data: "))
        objlist.insertleft(data)
    elif ch==3:
        objlist.deleteLeft()
    elif ch==4:
        objlist.deleteRight()
    elif ch==5:
        key=int(input("Enter key to be found: "))
        objlist.search(key)
    elif ch==6:
        key=int(input("Enter key to be deleted"))
        objlist.deleteKey(key)
    elif ch==7:
        objlist.printList()
    elif ch==8:
        break
    else:
        print("Invalid Choice")
