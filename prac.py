class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack)==0:
            return -1
        else:
            self.stack.pop()

stack1=Stack()
stack1.push(13)
stack1.push(69)
stack1.pop()

    
        