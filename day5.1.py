amt=10000
wamt=int(input('enter withdrawl amount'))
if wamt<=amt and wamt%100==0 and wamt>=100:
    amt=amt-wamt
    print('Amount withdraw is',wamt)
    print('Balance amount is',amt)
else:
    print('Invalid amout or not multiple of 100')
