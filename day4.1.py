amt=10000
wamt=int(input('enter amount to withdraw'))
if wamt%100==0:
    if wamt<=amt:
        if wamt>=100:
           amt=amt-wamt
           print('Amount withdraw is ',wamt)
           print('Balance amount is',amt)
        else:
            print('Invalid amount amount should be more than 100')
    else:
        print('Insufficient funds ')
else:
    print('Amount should multiple of 100')
