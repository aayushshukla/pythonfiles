list1=[10,30,50,60]
list2=[1,2,3,2]
list3=[]
for i in range(len(list1)):
    for j in range(list2[i]):
        list3.append(list1[i])

print(list3)
    

