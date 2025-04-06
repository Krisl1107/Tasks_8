n=int(input())
i=1
while i<n-1:
    i+=1
    if i%2!=0 and i%3!=0 and i!=2 and i!=3:
        print(i)
    elif i==2 or i==3:
        print(i)
    else:
        None
