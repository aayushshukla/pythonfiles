import random
nlist=['rock','paper','scissor']
position=random.randint(0,len(nlist)-1)
computer=nlist[position]
player=input('choose one from rock ,paper, or scissor')
if player==computer:
    print('Tie')
elif player=='rock':
    if computer=='paper':
        print('computer wins papers wrap rock')
    else:
        print('player wins rock smashes')
elif player=='paper':
    if computer=='scissor':
        print('computer jeet gya scissor cuts paper')
    else:
        print('player jeet gya paper wraps')
elif player=='scissor':
    if computer=='rock':
        print('computer wins tumse na ho payega rock smashes')
    else:
        print('playes wins bhut tez ho rahe ho scissor cuts')
else:
    print('Kuch bhi nahi wrong choice ')
