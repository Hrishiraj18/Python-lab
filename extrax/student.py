class Student:
    def __init__(self):
        self.student=[]
    def add(self,name):
        self.student.append(name)
    def display(self):
        for items in self.student:
            print(items)
    def search(self,name):
        if name in self.student:
            print("The item is present")
        else:
            print("the item is absent")
    def remove(self,name):
        self.student.remove(name)
s=Student()
flag=1
while flag!=0:
    flag=int(input("1.add\n2.display\n3.search\n4.remove\n"))
    if flag==1:
        n=input("Enter a name")
        s.add(n)
    elif flag==2:
        s.display()
    elif flag==3:
        n=input("Enter a name")
        s.search(n)
    elif flag==4:
        n=input("Enter a name")
        s.remove(n)
    elif flag==0:
        print("come back soon")
    else:
        print("Invalid choice")