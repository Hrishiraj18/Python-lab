class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __mul__(self,other):
        return self.a*other.a,self.b*other.b
    def __str__(self):
        return self.a,self.b
o1=complex(1,2)
o2=complex(2,3)
o3=o1*o2
print(o3)
        