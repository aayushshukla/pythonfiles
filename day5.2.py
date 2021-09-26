print('Enter PAN for pancard')
print('Enter ADHAAR for adhaar card')
idtype=input('enter id type')
if idtype=='PAN' or idtype=='ADHAAR':
    idno=input('enter id no')
    print(f'{idtype} no is {idno}')
else:
    print('Not a valid id')
