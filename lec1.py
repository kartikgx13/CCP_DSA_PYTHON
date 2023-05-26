"""list=[1,2,3,4,5,6,7,8,9]

for i in range(0,4):
    print(list[i])

for i in range(len(list)):
    print(list[i])

for i in list:
    print(i)


count=int(input("Enter numbers and their count you want to append"))
print("Enter each number: ")
for i in range(count):
    list.append(int(input()))

print(list)

print(list[-1])

list.sort()
print(list)"""

list1=[i for i in range(1,50,2)]
print(list1)
sum1=1

for i in range(len(list1)):
    sum1 = sum1 * int(list1[i])

print(sum1)
print(sum(list1))