with open("odd.txt","w")as f:
    l=[i for i in range(51) if i%2!=0]
    print(l)
    for i in l:
        f.write(str(i)+"\n")
with open("even.txt","w")as f1:
    l1=[i for i in range(51) if i%2==0]
    print(l1)
    for i in l1:
        f1.write(str(i)+"\n")
with open("new.txt","w")as a:
    with open("odd.txt")as a1:
        x=a1.readlines()
        y=[i.strip() for i in x]
        print(y)
        for i in y:
            if int(i)<26:
                a.write(i+"\n")
with open("new.txt","a")as a:
    with open("even.txt")as a1:
        x=a1.readlines()
        y=[i.strip() for i in x]
        print(y)
        for i in y:
            if int(i)<26:
                a.write(i+"\n")
