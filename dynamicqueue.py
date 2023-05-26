class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class DynamicQueue:
    def __init__(self):
        self.front=self.rear=None #since intially both the front and rear coincide hence both point to none
    
    def dequeue(self):
        if self.front==None:         #if front is not pointing to any node hence queue is empty
            print("Queue is empty")
        else:
            temp=self.front
            self.front=self.front.next
            print(f"Deleted data is: {temp.data}")   

    def enqueue(self,data):
        n=Node(data)
        if self.front==None:
            self.front=self.rear=n
        else:
            self.rear.next=n         #since we are inserting towards the right of the node hence setting rear next to n and making the inserted element the new rear
            self.rear=n 
    
    def printQueue(self):
        if self.front==None:
            print("Queue is empty")
        else:
            temp=self.front
            while(temp!=None):
                print(f"|{temp.data}|-->",end='')
                temp=temp.next
    
objqueue=DynamicQueue()
while True:
    print(f"1.Enqueue 2.Dequeue 3.Print 4.Exit")
    ch=float(input("Enter your choice: "))
    if ch==1:
        data=int(input("Enter data: "))
        objqueue.enqueue(data)
    elif ch==2:
        objqueue.dequeue()
    elif ch==3:
        objqueue.printQueue()
    elif ch==4:
        break
    else:
        print("Invalid choice")
