p,n=0,0
while ni!=0:
    ni=int(input())
    if ni>0:
        p+=1
    elif ni<0:
        n+=1
    else:
        break
print(f'Positive = {p} Negative = {n}')