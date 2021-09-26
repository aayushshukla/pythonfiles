n=int(input('enter no to check'))
i=2
st=0
while  i<n:
    if n%i==0:
        st=1
        break
    i=i+1

if st!=0:
    print('Not prime')
else:
    print('Prime')
