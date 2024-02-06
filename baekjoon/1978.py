N = int(input())
num = list(map(int,input().split()))
num.sort()
is_prime = [True] * (num[-1]+1)
is_prime[0] = is_prime[1] = False
prime = []
for n in range(2,num[-1]+1):
    if is_prime[n]:
        prime.append(n)
        for i in range(2 * n,num[-1]+1 , n):
            is_prime[i] = False
cnt = 0
for n in num:
    if n in prime:
        cnt+=1
print(cnt)
