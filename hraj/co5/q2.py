with open("cars.txt") as f:
    con=f.readlines()
    with open("cars1.txt","w") as f1:
        for i in range(0,len(con)):
            if(i%2!=0):
                f1.write(con[i-1])
with open("cars1.txt") as x:
    c=x.read()
print(c)

