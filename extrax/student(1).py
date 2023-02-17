class Student:
    def __init__(self):
        self.student={}
    def add(self,name,rollno):
        self.student[rollno]=name
    def display(self):
        for keys,values in self.student.items():
            print(f"The Roll no is {keys} and name is {values}")
    def search(self,rollno):
        if rollno in self.student:
            print(f"{self.student[rollno]} is present")
        else:
            print("the item is absent")
    def remove(self,rollno):
        del self.student[rollno]
s=Student()
flag=1
while flag!=0:
    flag=int(input("1.add\n2.display\n3.search\n4.remove\n"))
    if flag==1:
        r=int(input("Enter roll number"))
        n=input("Enter a name")
        s.add(n,r)
    elif flag==2:
        s.display()
    elif flag==3:
        r=int(input("Enter roll nn "))
        s.search(r)
    elif flag==4:
        r=int(input("Enter roll no "))
        s.remove(r)
    elif flag==0:
        print("come back soon")
    else:
        print("Invalid choice")