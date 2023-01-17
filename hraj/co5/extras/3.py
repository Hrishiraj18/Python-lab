import csv
with open("movies.csv","w",newline='')as x:
    y=csv.writer(x)
    y.writerow(["SN","Movies","Year"])
    y.writerow(["1","The Transporter","2012"])
    y.writerow(["2.","HP","2008"])
with open("movies.csv") as x:
    y=csv.reader(x)
    for row in y:
        print(','.join(row))