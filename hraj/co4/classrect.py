class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def find_area(self):
        area=self.length*self.breadth
        return area
    def find_perimeter(self):
        perimeter=2*(self.length+self.breadth)
        return perimeter
l1=int(input("Enter the length of the rectangle 1"))
b1=int(input("Enter the breadth of the rectangle 1"))
obj1=Rectangle(l1,b1)
l2=int(input("Enter the length of the rectangle 2"))
b2=int(input("Enter the breadth of the rectangle 2"))
obj2=Rectangle(l2,b2)
print("The Area of the rectangle is",obj1.find_area())
print("The Perimeter of the rectangle ",obj1.find_perimeter())
print("The Area of the rectangle is",obj2.find_area())
print("The Perimeter of the rectangle ",obj2.find_perimeter())
if obj1.find_area()>obj2.find_area():
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")
    
    
    