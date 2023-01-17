#(a)
print("A PART")
numbers=[-8,-26,22,50,55,-44,2,-13,1,21,48,36,99,-100,100]
numbers_c=[i for i in numbers if i>=0]
print(numbers_c)
print("B PART")
print("Enter the number upto which is square value is to be found")
n=int(input("enter a number"))
lis=[item**2 for item in range(1,n+1)] 
print("The square upto number ",n,"is ",lis)
print("C PART")
print("Enter the string whose vowels are to be listed")
c=input("enter the string:")
x=[i for i in c if i in'aeiou']
print("The list of vowels are",x)
print("D PART")
print("enter the string whose unicode value is to be found")
n=input("Enter the string: ")
z=[ord(i) for i in n]
print("The unicode value of the word ",n,"is" ,z)

