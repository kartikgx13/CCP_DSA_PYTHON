class Queue:
    def createQueue(self,size):
        self.q=[]
        self.front=0
        self.rear=-1
        self.Maxsize=size  #5
        for i in range(self.Maxsize):
            self.q.append(0) #[0,0,0,0,0]

    def Enqueue(self,e):
        self.rear+=1
        self.q[self.rear]=e
        #accept and sort
        self.q.sort(reverse=True)   #self.q=sorted(self.q)

    def isFull(self):
        if self.rear==self.Maxsize-1:
            return True
        else:
            return False
    def Dequeue(self):
        temp=self.q[self.front]
        self.front+=1
        return temp
    def isEmpty(self):
        if self.front>self.rear:
            return True
        else:
            return False
    def printQueue(self):
        for i in range(self.front,self.rear+1,1):
            print(self.q[i],end="--")
obj=Queue()
obj.createQueue(int(input("Enter size:")))
while True:
    print("1.Enqueue\n2.Dequeue\n3.Print\n0.Exit")
    ch=int(input("Enter:"))
    if ch==1:
        if obj.isFull()!=True:
            data=int(input("Enter data:"))
            obj.Enqueue(data)
            print("Element Enqueued")
        else:
            print("List Full")
    elif ch==2:
        if obj.isEmpty()!=True:
            print("Element dequeued:",obj.Dequeue())
        else:
            print("List Empty")
    elif ch==3:
        if obj.isEmpty()!=True:
            print("Elements in Queue")
            obj.printQueue()
        else:
            print("List Empty")
        
    elif ch==0:
        break
    else:
        print("Wrong input")