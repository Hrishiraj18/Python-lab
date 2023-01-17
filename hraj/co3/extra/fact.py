def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
n=int(input("Enter the number whose factorial is to be found"))
factorial(n)
