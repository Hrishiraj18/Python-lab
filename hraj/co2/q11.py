n1=int(input("Enter the length of square:"))
areasquare=lambda x:x*x
print("Area=",areasquare(n1))


n2=int(input("Enter the length of rectangle:"))
n3=int(input("Enter the breadth of rectangle:"))
arearect=lambda a,b:a*b
print("Area=",arearect(n2,n3))


n4=int(input("Enter the base of traingle:"))
n5=int(input("Enter the height of traingle:"))

areatra=lambda x,y:.5*x*y
print("Area=",areatra(n4,n5))
