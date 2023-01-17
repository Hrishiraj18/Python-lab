l=[]
n=int(input("Enter the number of items in list"))
for i in range(n):
    num=int(input("enter no "))
    l.append(num)
print(l)
add=0
for i in range(len(l)):
    add=add+l[i]
print("The sum of ",n,"items in a lsit is",add)
    
