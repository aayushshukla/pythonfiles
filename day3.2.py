pin=1234
upin=int(input('enter pin'))
# there will no statement between body of if and else
# there will be no else without if 

if pin==upin:
    print('Valid Pin')
    print('Enter 1 to withdraw')
    print('Enter 2 to deposite')
    print('Enter 3 to balance check')

else:
    print('Invalid pin')
