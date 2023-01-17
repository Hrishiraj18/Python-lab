st=input("enter the string")
x=list(st)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))
