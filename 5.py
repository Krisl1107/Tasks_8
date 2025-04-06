N=2
p=int(input())
k_1=0
k=[]

while N<p:
 N=N+1
 for i in range(1,N):
    if N%i==0:
        n_1=i
        if n_1!=N:
            k.append(n_1)

 if sum(k)==N:
     k_1+=1
print(k_1)
