list1=[1,2,3,4,5,6]
list2=[5,6,7,8,9,10,11]
if (len(list1))==(len(list2)):
    print("The lsit are of same length\n")
else:
    print("the list are of different length\n")
print("The length of list 1 is: ",len(list1),"the length of list 2 is: ",len(list2))
if((sum(list1))==(sum(list2))):
    print("\nThe sum are same\n")
else:
    print("\nthe sum are different\n")
print("The sum of list 1 is: ",sum(list1),"the sum of list 2 is: ",sum(list2))
set1=set(list1)
set2=set(list2)
setin=set1.intersection(set2)
if(setin!=0):
    print("The both set have some same values\n")
else:
    print("the both set have diffferent values\n")
print("The value that occur both is :",setin)

