N = int(input())
k=0
for n in range(1, N + 1):
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum += i
    if sum == n:
      k+=1
print(k)
