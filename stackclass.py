class CreateStack:
    tos=-1
    maxSize=0
    stack=[]

    def enterSize(self,maxSize):
        self.maxSize=maxSize
    
    def printStack(self):
        if self.tos==-1:
            print("Stack is empty")
        else:
            for i in range(len(self.stack)-1,-1,-1):
                #we have to print the array in reverse order to print the stack hence
                #we started from the end and continued till -1 as it is the initial
                #value of the top of the stack
                print(self.stack[i])
    
    def pushElement(self):
        if (self.tos==self.maxSize-1):
            print("Stack is full")
        else:
            self.stack.append(int(input("Enter data: ")))
            self.tos += 1
    
    def popElement(self):
        if (self.tos==-1):
            print("Stack is empty")
        else:
            self.stack.pop()
            self.tos -= 1
    
    def peek(self):
        if (self.tos==-1):
            print("No element")
        else:
            print(self.stack[-1])
    
objstack=CreateStack()
size=int(input("Enter max size"))
objstack.enterSize(size)

while True:
    print(f"1.Push 2.Pop 3.Print 4.Peek 5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        objstack.pushElement()
    elif ch==2:
        objstack.popElement()
    elif ch==3:
        objstack.printStack()
    elif ch==4:
        objstack.peek()
    elif ch==5:
        break
    else:
        print("Invalid choice")