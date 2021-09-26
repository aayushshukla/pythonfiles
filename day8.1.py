# Dynamic size , Indexed Indexing positive or negative
# Postive indexing starts from 0
# Negative indexing starts from -1 and from the end of the list
# Ordered , Duplicacy , Heterogenous 
# Mutable  that can be changed or modified .
# if we write anything in [] it becomes list
# or we can use list() to create a list

l=[]
print('Type of l',type(l))
l =[10,20,30,40,50,10]

print(f'size of list {len(l)}')
#Access element of list listname[index] if index in range it will return value
# at given index and if index not in range it will raise error
index=int(input('enter index'))
print(f'value at given index {index} is {l[index]}')
#Update element in a list listname[index] =value
v=int(input('enter value at given index to update'))
print('List before update is',l)
l[index]=v
print('List after update',l)
for i in l:
    print(i)

#append(object) it will add a new at the end of list
ne=int(input('enter new value to add in a list'))
l.append(ne)
print('List after adding new value ',l)
