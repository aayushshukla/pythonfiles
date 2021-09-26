n=int(input('enter number'))
st=0

for i in range(2,n):
    if n%i==0:
        st=1
        break

if st!=0:
    print('Not prime')
else:
    print('Prime')
