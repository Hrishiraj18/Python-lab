class Vending:
    def __init__(self,name):
        self.milk=2000
        self.water=3000
        self.coffeepowder=100
        self.teapowder=100
        self.sugar=50
        self.name=name

class Produce(Vending):
    def tea(self):
        if self.milk>250 and self.water >250 and self.teapowder>20 and self.sugar>10:
            self.milk-=250
            self.water-=250
            self.teapowder-=20
            self.sugar-=10
            print(f"{self.name} please collect your order")
        else:
            print("Please fill up the machine")
            print()
            print()

    def coffee(self):
        if self.milk>250 and self.water >250 and self.coffeepowder>20 and self.sugar>10:
            self.milk-=250
            self.water-=250
            self.coffeepowder-=20
            self.sugar-=10
            print(f"{self.name} please collect your order")
        else:
            print("Please fill up the machine")
            print()
            print()
    def display(self):
        print(f"Milk: {self.milk} Water: {self.water} Coffee powder : {self.coffeepowder} Tea powder:{self.teapowder} Sugar : {self.sugar}")

user=Produce("Hrishi")
flag=1
while(flag!=0):
    flag=int(input("1.Cofee \n2.Tea\n3.Display\n0.Exit\n"))
    if flag==1:
        user.coffee()
    elif flag==2:
        user.tea()
    else:
        user.display()