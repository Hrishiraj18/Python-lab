s=int(input("Enter the number whose factorial is to be found"))
fact=1
if(s==0):
    print("the factorial is 1")
else:
    for i in range(1,s+1):
        fact=fact*i
print("Fact of",s,"is",fact)
