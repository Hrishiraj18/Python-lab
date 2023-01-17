import csv
with open("student.csv") as f:
    x=csv.reader(f)
    next(f)
    next(f)
    total=0
    for row in x:
        print(row[2])