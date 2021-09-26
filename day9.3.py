list1=[10,20,40,10,50,10,50,10]
#count(element) it will return no of occurance of given element
# if element not exists it return 0
e=int(input('enter element to count'))
c=list1.count(e)
print(f'No of occurance of {e} in list is {c}')
#index(element) it will return index position of first occurance of given element
#if element not exists it will raise error
es=int(input('enter element to find '))
pos=list1.index(es)
print(f'Element {es} 1 time found at {pos}')
#remove(element) remove first occurance of given element from  a list
# if element element not found it raise error
re=int(input('enter element to remove'))
print('List before remove',list1)
list1.remove(re)
print('List after remove',list1)
#reverse() it will reverse a list
list1.reverse()
print('Reverse list is',list1)
#clear() it will remove all elements of list and return an empty list
list1.clear()
print('List after clear',list1)

