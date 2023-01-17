n=int(input("Enter the upper limit up to which FIBONACCI sequence is to be found"))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    s=a+b
    print(s)
    a=b
    b=s
