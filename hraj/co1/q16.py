name1=input("Enter string 1\n")

name2 = input("Enter string 2\n")
x = name1[0:1]
name1= name1.replace(name1[0:1],name2[0:1])
name2= name2.replace(name2[0:1],x)
print("The result is")
print(f"{name1} {name2}")
