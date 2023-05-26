keys=[]
n=int(input("Enter max no. of keys:"))
for i in range(n):
    data=input("Enter key: ")
    keys.append(int(data))
hashTable=[]
for i in range(10):
    hashTable.append(0)
modValues=[]
for i in range(n):
    modValues.append(keys[i]%10)
