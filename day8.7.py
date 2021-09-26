run=[1000,500,30]
match=[100,50,1]
avg=[]
for i in range(len(run)):
    avrrun=run[i]/match[i]
    avg.append(avrrun)
print('Avg is',avg)
