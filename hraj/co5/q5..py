import csv
colum_val=["sn","Player","No"]
data=[
    {"sn":1,"Player":"virat","No":18},
    {"sn":2,"Player":"abd","No":17},
    {"sn":3,"Player":"msd","No":7},
    {"sn":4,"Player":"rohith","No":45},
    {"sn":5,"Player":"gayle","No":333}
]
try:
    with open("xyz.csv","w")as x:
        writer=csv.DictWriter(x,fieldnames=colum_val)
        writer.writeheader()
        for x in data:
            writer.writerow(x)
except IOError:
    print("Input output error")
with open("xyz.csv") as x:
    for line in csv.DictReader(x):
        print(line)