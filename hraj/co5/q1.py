with open("cars.txt") as f:
    con=f.readlines()
print(con)
x=[y.strip() for y in con]
print(x)