s=input("Enter the strings separated by space")
l=s.split()
print(l)
n=len(l[0])
x=l[0]
for i in l:
    if len(i)>n:
        x=l[i]
print("The longest word is ",x)
        
