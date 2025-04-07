N = int(input())
for num in range(1, N + 1):
    sum_of_divisors = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        print(num)
