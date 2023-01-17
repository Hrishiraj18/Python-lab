n=int(input("enter the limit"))
n1=0
n2=1
count=0
if n<=0:
    print("Enter a positive number")
elif n==1:
    print("fibonacci sequence upto",n,"is",n1)
else:
    print("fibonacci sequence upto ",n,"is")
    while count<n:
        print(n1)
        x=n1+n2
        n1=n2
        n2=x
        count=count+1
