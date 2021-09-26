for i in range(0,4):
    x=97
    for j in range(0,4):
        if i>=j:
            print(chr(x),end='')
            x=x+1
    print()
