n=int(input("Enter the number"))
fact=1
i=1
if(n==0):
    print("the factorial is 1")
else:
    while i<=n:
        
        fact=fact*i
        i=i+1
print("Factorial of",n,"is",fact)

