string=input("Enter a string ending with ing or ly")
if string[-3:]=="ing":
    string+="ly"
else:
    string+="ing"
print(string)
