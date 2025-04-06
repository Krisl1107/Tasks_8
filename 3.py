k=0
m=1
n=[]
while m!=0:
    m=float(input())
    k+=1
    n.append(m)
print(n)
print(sum(n)/(k-1))
