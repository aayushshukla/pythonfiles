l=[10,20,30,40]
#insert(index,value) it will add value at given index .A new value will be added
# if given index is out of range than value will added at the end of list 
print('List before insert',l)
ind=int(input('enter index position'))
v=int(input('enter value at given index'))
l.insert(ind,v)
print('List after insert',l)
