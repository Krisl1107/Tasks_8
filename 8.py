z=""
for i in range(1,10):
        k=z+str(i)
        m=int(k)*8+i
        print(k,"* 8 + ",i,"=",m)
        z=k
z=""
for i in range(1,10):
        k=z+str(i)
        m=int(k)*9+i+1
        print(k,"* 9 + ",i+1,"=",m)
        z=k
