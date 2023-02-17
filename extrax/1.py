data_list = [1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,"key2":[55,67,78,89],4:(45,22,61,34)},[56,"data science"],"Machine learning"]
list1=[]
def convert(data_list):
    for i in data_list:
        print(type(i))
        if type(i)==int:
            list1.append(i)
        if type(i)==list:
            convert(list(i))
        if type(i)==bool:
            list1.append(i)
        if type(i)==tuple:
            list1.extend(list(i))
        if type(i)==set:
            list1.extend(list(i))
        if type(i)==dict:
            keys=list(i.keys())
            value=list(i.values())
            convert(keys+value)
convert(data_list)
print(list1) 
ix=1
for i in list1:
    ix=ix*i
print(ix)       