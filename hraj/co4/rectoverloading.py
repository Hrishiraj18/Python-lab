class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
        self.area=self.__length*self.__breadth
    def __lt__(self,other):
        return self.area<other.area
l1=int(input("Enter the length of the rectrangle 1: "))
b1=int(input("enter the breadth of the rectangle 1: "))
l2=int(input("Enter the length of the rectrangle 2: "))
b2=int(input("enter the breadth of the rectangle 2: "))
obj1=Rectangle(l1,b1)
obj2=Rectangle(l2,b2)
if obj1>obj2:
    print("Area of first Rectangle is greater")
else:
    print("Area of second Rectangle is greater")