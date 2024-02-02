def prime_search(limit):
    primes = [True]*(limit+1)
    primes[0]=primes[1]=False
    for n in range(2,int(limit**0.5)+1):
        if primes[n]:
            for i in range(n*n,limit+1,n):
                primes[i] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]


N = int(input())
primes = prime_search(2000)
num = list(map(int,input().split()))
for i in range(1 << len(num)):
    sum_num = 0
    count= 0
    for j in range(len(num)):
        if i & (1 << j):
            sum_num += num[j]
            count += 1
            if count==3:
                print(j,end='')
        print(',')
    # if sum_num in primes and count == 2:


