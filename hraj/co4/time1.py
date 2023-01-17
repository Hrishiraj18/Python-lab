class time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        __sum1 = (self.__hour * 60 * 60) + (self.__minute * 60) + (self.__second)
        __sum2 = (other.__hour * 60 * 60) + (other.__minute * 60) + (other.__second)
        __sum_time = __sum1 + __sum2
        __hour_conv = int(__sum_time / 3600)
        __min_conv = int((__sum_time % 3600) / 60)
        __sec_conv = int((__sum_time % 3600) % 60)
        return "{0} hours, {1} minutes, {2} seconds".format(__hour_conv, __min_conv, __sec_conv)
print("Enter Time - 1")
h1=int(input("Enter the hour"))
m1=int(input("Enter minute"))
s1=int(input("Enter second"))
print("Enter Time - 2")
h2=int(input("Enter the hour"))
m2=int(input("Enter minute"))
s2=int(input("Enter second"))
t1 = time(h1,m1,s1)
t2 = time(h2,m2,s2)

print(t1+t2)