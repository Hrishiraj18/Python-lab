import csv
with open("cars.csv") as fx:
    my=csv.reader(fx)
    for x in my:
        print(x)