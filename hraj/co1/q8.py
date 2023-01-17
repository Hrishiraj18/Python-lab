str1="onion"
print("The original string is ",str1)
word="$"
result=str1[0]+str1[1:].replace(str1[0],word)
print("the replaced string is" +str(result))
