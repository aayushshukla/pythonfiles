n1=int(input('enter no 1'))
n2=int(input('enter no 2'))
print('Enter + to add')
print('Enter - to sub')
print('Enter * to mul')
print('Enter / to div')
ch=input('enter your choice')
if ch=='+':
    print(f"{n1}+{n2} = {n1+n2}")

if ch=='-':
    print(f"{n1}-{n2} = {n1-n2}")

if ch=="*":
    print(f"{n1}*{n2} = {n1*n2}")

if ch=="/":
    if n2!=0:
        print(f"{n1}/{n2} = {n1/n2}")
    else:
        print('can not divide by 0')
