lis=[]
oddlist=[]
n=int(input("Enter the number of entries in the list"))
print("enter the numbers")
for item in range(n):
    num=int(input("no"))
    lis.append(num)
print(lis)
for item in lis:
    if(item%2!=0):
        oddlist.append(item)
print("the odd entries are ",oddlist)
