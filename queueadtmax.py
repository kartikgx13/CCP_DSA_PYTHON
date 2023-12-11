class CreateQueue:
    queue=[]
    front=0
    rear=-1
    maxSize=0
    def enterSize(self,maxSize):
        self.maxSize=maxSize                               
    
    def printQueue(self):
        if (self.front>self.rear): #since intially front = 0 and rear = -1 
            print("Queue is empty")
        else:
            for i in range(0,len(self.queue)):
                print(self.queue[i]) #we will print the array in normal order only
    
    def enqueue(self):
        if (self.rear==(self.maxSize-1)):
            print("Queue is full")
        else:
            self.queue.append(int(input("Enter data: ")))
            self.rear += 1
    
    def dequeue(self):
        if (self.front>self.rear):
            print("Queue is empty")
        else:
            self.queue.pop(0)
            self.front += 1

objqueue=CreateQueue()
size=int(input("Enter max size"))
objqueue.enterSize(size)

while True:
    print(f"1.Enqueue 2.Dequeue 3.Print 4.Exit")
    ch=float(input("Enter your choice: "))
    if ch==1:
        objqueue.enqueue()
    elif ch==2:
        objqueue.dequeue()
    elif ch==3:
        objqueue.printQueue()
    elif ch==4:
        break
    else:
        print("Invalid choice")