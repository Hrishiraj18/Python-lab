class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
        
    def __add__(self,other):
        s=(self.__second+other.__second)%60
        m=(self.__minute+other.__minute+int((self.__second+other.__second)/60))%60
        h=(self.__hour+other.__hour+int((self.__minute+other.__minute)/60))%24
        return h,m,s
    def __str__(self):
        print("Time:",self.__hour,":",self.__minute,":",self.__second)


h1=int(input("Enter the time in hour,minute and second"))
m1=int(input())
s1=int(input())
h2=int(input("Enter the time in hour,minute and second"))
m2=int(input())
s2=int(input())
time1=Time(h1,m1,s1)
print(time1.__str__())
time2=Time(h2,m2,s2)
print(time2.__str__())
total=time1+time2
print("The total time is ",total)
    
        