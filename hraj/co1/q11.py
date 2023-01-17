print("Enter three numbers\n")
a=int(input("Enter value of a\n"))
b=int(input("Enter value of b\n"))
c=int(input("Enter value of c\n"))
if((a>b)and(a>c)):
   print(a,"is the greatest")
elif((b>a)and(b>c)):
     print(b,"is the greatest")
else:
     print(c," is the greatest")
