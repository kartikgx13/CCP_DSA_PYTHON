class HashTable:
    maxSize=10
    hashEntry=[]
    elementCount=0

    def __init__(self):
        for _ in range(self.maxSize):
            self.hashEntry.append(int(0))
        
    
    def isFull(self):
        if self.elementCount==self.maxSize:
            return True
        else:
            return False
    
    def hashFunction(self,key):
        return key%self.maxSize
    
    def insertKey(self,key):
        if self.isFull()==True:
            print("Hash table is full")
            return

        self.isStored=False
        self.position=self.hashFunction(int(key))
        #checking if position is empty
        if self.hashEntry[self.position]==0:
            self.hashEntry[self.position]=key
            print(f"{key} inserted at position {self.position}")
            self.isStored=True
            self.elementCount += 1
        else:  #if the above case is not true then collision has taken place hence this else part will be executed
            print(f"Collision occured for element {key} at position {self.position} hence finding new position")
            while (self.hashEntry[self.position]!=0):
                self.position += 1
                if (self.position>=self.maxSize):
                    self.position=0
            self.hashEntry[self.position]=key
            self.isStored=True
            self.elementCount += 1
        return

    def searchElement(self,key):
        self.found=False
        self.position=self.hashFunction(key)
        if (self.hashEntry[self.position]==key):
            self.found=True
            return self.position
        else:
            self.temp=self.position-1
            while (self.position<self.maxSize):
                if (self.hashEntry[self.position]!=key):
                    self.position += 1
                else:
                    return self.position
            
            self.position=self.temp
            while(self.position>=0):
                if (self.hashEntry[self.position]!=key):
                    self.position -= 1
                else:
                    return self.position
        
        if (self.found==False):
            print("Not found")
            return -1
    
    def deleteElement(self,key):
        self.position=self.searchElement(key)
        if(self.position!=-1):
            self.hashEntry[self.position]=0
            print(f"Deleted entry: {key}")
            self.elementCount-=1
        else:
            print("Element was not in hash table")
        return
    
    def displayTable(self):
        for item in self.hashEntry:
            print(item)
        print(f"The no. of elements in the table are: {self.elementCount}")

table1=HashTable()
while True:
    print("\n 1.Insert Key \n 2.Search key \n 3.Delete key \n 4.Print Table \n 5.Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        data=int(input("Enter key to be inserted: "))
        table1.insertKey(data)
    elif ch==2:
        data=int(input("Enter key to be searched: "))
        table1.searchElement(data)
    elif ch==3:
        data=int(input("Enter key to be deleted: "))
        table1.deleteElement(data)
    elif ch==4:
        table1.displayTable()
    elif ch==5:
        break
    else:
        print("Invalid choice")

