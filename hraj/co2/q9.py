n=int(input("enter the number"))
x=int(n/2)
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
for i in range(x+1,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
