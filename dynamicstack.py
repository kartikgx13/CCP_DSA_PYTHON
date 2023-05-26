class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class DynamicStack:
    def __init__(self):
        self.tos=None
    def push(self,data):
        n=Node(data)
        if self.tos==None:   #if head is empty insert n
            self.tos=n
        else:               #suppose if a element is already present then set its next to old head and make the inserted element as new head
            n.next=self.tos
            self.tos=n
    
    def pop(self):
        if self.tos==None:
            print("Stack is Empty")
        else:
            temp=self.tos             #store the head that is the top of the stack in a temp variable then set the next element as new head so top of the stack will be deleted
            self.tos=self.tos.next
            print(f"Deleted Data : {temp.data}")  #storing in temp to display the deleted data

    def peek(self):
        if self.tos==None:
            print("Stack is empty")
        else:
            print(f"Top of the stack: {self.tos.data}")
    
    def printStack(self):
        if self.tos==None:
            print("Stack is empty")
        else:
            temp=self.tos
            while temp!=None:
                print(f"|{temp.data}|-->",end='')
                temp=temp.next
objstack=DynamicStack()
while True:
    print(f"1.Push 2.Pop 3.Print 4.Peek 5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter data: "))
        objstack.push(data)
    elif ch==2:
        objstack.pop()
    elif ch==3:
        objstack.printStack()
    elif ch==4:
        objstack.peek()
    elif ch==5:
        break
    else:
        print("Invalid choice")