class CreateQueue:
    queue=[]
    front=0
    rear=-1
    def printQueue(self):
        if (self.front>self.rear):
            print("Queue is empty")
        else:
            for i in range(0,len(self.queue)):
                print(self.queue[i])
    
    def enqueue(self):
        self.queue.append(int(input("Enter data: ")))
        self.rear += 1
    
    def dequeue(self):
        if (self.front>self.rear):
            print("Queue is empty")
        else:
            self.queue.pop(0)
            self.front += 1

objqueue=CreateQueue()
while True:
    print(f"1.Enqueue 2.Dequeue 3.Print 4.Exit")
    ch=int(input("Enter your choice: "))
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



    

