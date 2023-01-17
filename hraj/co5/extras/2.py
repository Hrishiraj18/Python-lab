with open("cars.txt") as f:
    with open("cars3.txt","w") as fw:
        for line in f.readlines():
            fw.write(line)