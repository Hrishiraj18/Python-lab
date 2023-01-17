months={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"Novembver":30,"December":31}
print(sorted(months.items()))
s=input("Enter the month")
print(months[s])
s1=input("enter the month to be removed")
del months[s1]
print("Dictionary after removing month")
print(months)
s2=input("enter month which need to be addded")
s3=input("enter the days of month")
months[s2]=s3
print(months)


