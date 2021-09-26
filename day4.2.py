pin=1234
upin=int(input('enter user pin'))
amt=10000
if pin==upin:
    print('Enter 1 to withdraw')
    print('Enter 2 to deposite')
    print('Enter 3 to check balanace')
    ch=int(input('enter operation'))
    if ch==1:
        print('welcome to withdraw money')
        wamt =int(input('enter withdraw amount'))
        if wamt%100==0:
            if wamt>=100:
                if wamt<=amt:
                    print('Enter 1 for 2000 ')
                    print('Enter 2 for 500')
                    print('Enter 3 for 100')
                    ton =int(input('enter your choice of note '))
                    amt=amt-wamt
                    print('withdraw amount is ',wamt)
                    print('Balance amount is',amt)
                else:
                    print('Insufficient funds')
            else:
                print('invalid amount')
        else:
            print('Amount should be in rs 100, 200 or 500')
    elif ch==2:
        pass 
        
    elif ch==3:
        print('Amount is',amt)
    else:
        print('Invalid operation choosed ')


else:
    print('Invalid pin')
