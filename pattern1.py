for i in range(1,6):
    print(i*" * ")

for i in range(5):
    for j in range(5):
        print("* ",end="")
    print()

for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()

for i in range(4,-1,-1):
    for j in range(i+1):
        print("* ",end="")
    print()

for i in range(5):
    for j in range(i,5):
        print("* ",end="")
    print()


for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    
    for j in range(i+1):
        print("*",end="")
    
    print()

for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    
    for j in range(i,5):
        print("*",end="")
    
    print()


for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    
    for j in range(i):
        print("*",end="")
    
    for j in range(i+1):
        print("*",end="")
    
    print()
print("hello")
for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    
    for j in range(i,4):
        print("*",end="")
    
    for j in range(i,5):
        print("*",end="")
    
    print()