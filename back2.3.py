n1=int(input('enter number 1'))
n2=int(input('enter number 2'))

print('enter + to add')
print('enter - to sub')
print('enter * to mul')
print('enter / to div')
ch=input('enter your choice')

if ch=='+':
    print(f'{n1}+{n2}={n1+n2}')
elif ch=='-':
    print(f'{n1}-{n2}={n1-n2}')
elif ch=='*':
    print(f'{n1}*{n2}={n1*n2}')
elif ch=='/':
    if n2!=0:
        print(f'{n1}/{n2}={n1/n2}')
    else:
        print('Can not divide by zero')
else:
    print('Invalid choice')
