from itertools import combinations

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
num_lst=list(combinations(num,2))
for n in num_lst:
    if n[0]+n[1] not in primes:
        num_lst.remove(n)

print(num_lst)



