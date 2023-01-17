lis=[]
no=int(input("Enter the number of items"))
print("enter the numbers")
for item in range(no):
    num=int(input("no:"))
    lis.append(num)
print(lis)
for item in range(len(lis)):
    if(lis[item]>100):
        lis[item]="over"
print(lis)
