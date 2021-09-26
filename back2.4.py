n=int(input('enter no'))
if n%7==0:
    if n%9==0:
        print(n,'is divisible  by 7 and 9')
    else:
        print('No divisible by 9')
else:
    print('Not divisible by 7')
