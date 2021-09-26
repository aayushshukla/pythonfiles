l=[]
n=int(input('enter number of students'))
for i in range(n):
    n=int(input('enter name'))
    l.append(n)

s=0

for x in l:
    s=s+x
print('Sum of element is',s)
