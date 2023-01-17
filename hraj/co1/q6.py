l=[]
n=int(input("no of names"))
for i in range(n):
    name=input("enter the name")
    s=name.split()
    l.append(s[0])
s=0
for i in range(len(l)):
    count=l[i].count("a")
    s=s+count
print("The number of occurence of 'a' is",s)
